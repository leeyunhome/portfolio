# EBS 영어 회화 추출 파이프라인 (Whisper 기반)

> EBS 라디오 회차를 자동 다운로드 → **Whisper로 전사** → 음악 구간 분석으로 영어 대화만 정밀 추출 → 모바일 웹 플레이어로 배포하는 end-to-end AI 자동화 파이프라인.

!!! info "실제 서비스"
    개인 학습용으로 직접 만들어 운영 중인 프로젝트입니다.
    라이브 대시보드: [leeyunhome.github.io/ebs-learning](https://leeyunhome.github.io/ebs-learning/)

---

## 배경

EBS 라디오 왕초보 영어의 "전체 대화" 코너만 매일 자동으로 뽑아 듣고 싶었다.
30분짜리 방송에서 영어 회화는 1분 남짓 — 이 구간만 사람 손 없이 잘라내는 게 목표였다.

핵심 난이도는 두 가지였다:

1. **어디서부터가 영어 대화 구간인가?** — 방송마다 위치가 다름
2. **음성 인식 오류에도 강건하게 시작점을 찾을 수 있는가?**

---

## 시스템 구성

```
run.bat --episode N
     │
     ▼
┌────────────────────────────────────┐
│         runner.py (오케스트레이터)  │
│  Thread A: watcher (파일 감시·추출) │
│  Thread B: auto_download (Playwright)│
└──────────┬──────────────┬───────────┘
           │ polls        │ controls
           ▼              ▼
     watch dir  ◀──drops── EBS 웹 + 데스크탑 다운로더
           │ new MP3
           ▼
┌────────────────────────────────────┐
│      extractor.py (추출 엔진)       │
│  ① 한국어 Whisper 전사 (앵커 탐색)  │
│  ② inaSpeechSegmenter (음악/음성)   │
│  ③ 시작·종료점 결정                 │
│  ④ MP3 잘라내기                     │
│  ⑤ 영어 Whisper 재전사 → JSON 생성  │
└──────────┬─────────────────────────┘
           ▼
   Supabase (Storage + DB)
           ▼
   build_player.py → git push → GitHub Pages
```

---

## 사용한 AI 기술

| 기술 | 모델·라이브러리 | 역할 |
|---|---|---|
| **음성 인식 (ASR)** | faster-whisper `large-v3-turbo` (ctranslate2/GPU) | 한국어·영어 전사 |
| **오디오 구간 분석** | inaSpeechSegmenter (TensorFlow 기반) | 음악/음성 구간 라벨링 |
| **퍼지 매칭** | N-gram(trigram) Sørensen-Dice 유사도 | ASR 오인식 보정 |

---

## 데이터 처리 과정 (5단계 추출)

### ① 한국어 전사로 "앵커" 찾기 — Cheap Pass

30분 방송 전체를 좋은 모델로 두 번 돌리면 느리고 비싸다.
그래서 먼저 **한국어 Whisper로 방송 후반부(21분~)만** 싸게 전사해서,
"전체 대화를 들어보겠습니다" 같은 진행자 멘트(앵커)의 종료 시각을 찾는다.

### ② ASR 오인식에 강한 앵커 검색

Whisper는 "전체대화"를 "전체되어"처럼 잘못 전사할 때가 있다.
이를 위해 **3단계 검색**을 둔다:

```
완전 일치  →  N-gram fuzzy(Sørensen-Dice)  →  인접 세그먼트 병합 재검색
```

한 세그먼트가 깨져도 인접 세그먼트와 합쳐서 회수한다.
자주 틀리는 변형은 `config.py`의 `ANCHOR_PHRASES`에 데이터로 미리 등록해 둔다.

### ③ 음악 구간으로 대화 경계 결정

`inaSpeechSegmenter`로 오디오 전체를 `(음악/음성, 시작, 끝)`으로 라벨링한다.
앵커 직후 **첫 음악 구간**을 대화 시작점으로, 이어지는 연속 한국어나 명시적 종료 문구를 종료점으로 잡는다.

### ④ 오디오 추출

`pydub`로 해당 구간만 잘라 모노·64kbps로 저장한다.

### ⑤ 영어 재전사 — Expensive Pass

잘라낸 **30~60초 클립만** 영어 Whisper로 고품질 재전사한다.
전체를 좋은 모델로 두 언어 돌리는 것보다 훨씬 빠르고 정확하다.
이후 한국어 잔여 제거·중복 제거·경계 정리 후처리를 거쳐 스크립트와 `player.json`을 만든다.

---

## 설계에서 얻은 것

- **Cheap-pass → Expensive-pass 다단 추론**: "먼저 위치를 찾고, 그다음 그 구간만 정밀 추론". 비디오 분석·OCR·긴 문서 검색 어디에나 적용되는 패턴.
- **외부 백엔드는 shim으로 격리**: faster-whisper를 openai-whisper와 동일한 dict 형태로 감싸, 모델·제공자 교체 비용을 한 파일로 국한.
- **파일시스템으로 파이프라인 디커플링**: 다운로더와 watcher가 서로의 API를 모른 채 공유 폴더로만 연결 — 단계별 재실행·디버깅이 쉬움.
- **실패를 조용히 넘기지 않기**: 앵커 검색 실패 시 "무엇을 config에 추가하면 되는지" 진단을 자동 출력.

---

## 현장에서 밟은 지뢰 (환경 이슈)

회사에서 TensorRT·CUDA 스택을 다루던 경험이 그대로 이어진 부분.

| 증상 | 원인 | 처방 |
|---|---|---|
| Python이 traceback 없이 종료 (`exit -1073741819`) | Windows ACCESS_VIOLATION — native crash | 라이브러리 버전 충돌 의심, 버전 핀 |
| `ctranslate2` 4.7 + Py3.9에서 무음 크래시 | 환경별 native crash | `ctranslate2==4.4.0`로 다운그레이드 |
| `cudnn_ops_infer64_8.dll` 못 찾음 | ctranslate2 4.4가 cuDNN 8 요구 | `nvidia-cudnn-cu12==8.9.*` 설치 + PATH |
| TF와 Whisper GPU 충돌 크래시 | 초기화 순서 | INA(TF/CPU) 먼저 → Whisper(GPU) 나중 |

> ML 라이브러리는 처음부터 `==` 버전 핀. `>=`는 미래의 나를 한밤중에 깨우는 버튼이다.
