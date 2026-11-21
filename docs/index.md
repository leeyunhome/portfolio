# 이윤호 · Applied AI / Embedded SW Engineer

<div style="font-size:1.15em; margin:0.8em 0 1.5em; line-height:1.7; color:var(--md-default-fg-color--light)">
SoC 레지스터부터 현장 라인 사이클, 그리고 3D·AI 서비스까지 —<br>
<strong>하드웨어와 소프트웨어를 넘나들어 현장 AI 추론 엔진을 배포·운영하고, 아이디어를 직접 제품으로 구현하는 엔지니어.</strong>
</div>

Edge SoC(Jetson, Hailo, Eyenix) 기반 비전 AI 시스템 배포·운영 경험 약 3년.
ONNX/TensorRT 추론 최적화, SoC 레지스터 레벨 디버깅, 93일 무중단 에이징 테스트, VLM/VLA 선행 연구부터
개인 오픈소스·웹 프로젝트 24종 직접 설계·배포까지 — 하드웨어 레이어부터 사용자 인터페이스까지 전 스택을 다룹니다.

<div class="grid cards" markdown>

-   :material-chip: **Edge SoC · 추론 최적화**

    NVIDIA Jetson(Orin NX/Xavier), Hailo-15H, Eyenix EN675/EN683 환경에서 TensorRT(FP16/INT8)·ONNX Runtime 기반 비전 파이프라인 최적화 및 배포

-   :material-shield-check: **93일 연속 가동 · 신뢰성**

    양산 전 CPU/GPU Full-load 93일 무중단 에이징 테스트 100% 통과, Memory Leak·발열 프로파일링, SonarQube·SBOM·국방/공공 보안 인증 대응

-   :material-rocket-launch: **24+ 직접 구현 프로젝트**

    3D Gaussian Splatting·디지털 트윈·커널 `perf/ftrace` 프로파일링·Whisper/Gemini 파이프라인·자체 SVG 슬라이드 엔진까지 end-to-end 구현

</div>

---

## 실무 핵심 사례 (Case Studies)

<div class="grid cards" markdown>

-   **SoC 레지스터 제어로 비전 데이터 무결성 확보**

    ---

    다단 추론 중 발생한 UYV 영상 파손 이슈를 소프트웨어 우회가 아닌
    **SoC 레지스터 직접 제어**로 근본 해결. 오검출 원천 차단.

    [:octicons-arrow-right-24: 자세히 보기](cases/01-soc-vision-integrity.md)

-   **93일 에이징 테스트 — 가동률 100% 달성**

    ---

    양산 투입 전 CPU/GPU Full-load 환경에서 **93일 연속 무중단 가동**.
    Memory Leak·발열 프로파일링 → SOP 수립으로 현장 신뢰성 입증.

    [:octicons-arrow-right-24: 자세히 보기](cases/02-aging-test.md)

-   **Jetson Orin NX에서 VLM/VLA 실시간 추론 검증**

    ---

    차세대 제조 로봇을 위한 멀티모달 AI 선행 연구.
    **Edge 환경에서 VLM 실시간 구동 가능성**을 성능 프로파일링으로 입증.

    [:octicons-arrow-right-24: 자세히 보기](cases/03-vlm-edge.md)

-   **글로벌 양산 수준의 SW 품질 및 보안 관리**

    ---

    SonarQube 정적 분석·SBOM·영문 AI SDK 문서화 및 배포 서비스 구축.
    국방·공공 보안 인증 기반 마련.

    [:octicons-arrow-right-24: 자세히 보기](cases/04-sw-quality.md)

-   **TensorRT 정밀도 벤치마크 — 실행 가능한 데모**

    ---

    PyTorch → ONNX → TensorRT(FP32/FP16/INT8) 변환 및 지연시간/FPS 측정.
    RTX 4060 환경에서 직접 재현 가능한 코드 포함.

    [:octicons-arrow-right-24: 자세히 보기](cases/05-trt-benchmark.md)

</div>

---

## 대표 개인 프로젝트 & 엔지니어링 랩

실무 외 시간에 직접 설계·배포한 프로젝트 중 핵심 작업입니다. 전체 24개 라이브 프로젝트는 [프로젝트 허브](https://leeyunhome.github.io/)에서 바로 체험할 수 있습니다.

<div class="grid cards" markdown>

-   **Jetson MLOps Lab — 비전 파이프라인 최적화**

    ---

    Jetson Orin 기반 비전 추론 파이프라인의 정량 벤치마킹, 모델 양자화·런타임 최적화 실험 노트북.

    [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/jetson-mlops-lab/){ target="_blank" }

-   **perf/ftrace 성능 프로파일링 — Jetson Orin**

    ---

    임베디드 리눅스 커널 레벨에서 `perf`·`ftrace`로 CPU/스케줄링 병목을 추적·분석한 프로파일링 기록.

    [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/jetson-perf-profiling/){ target="_blank" }

-   **mxd-twin — 복합단지 3D 디지털 트윈**

    ---

    3D 공간 재구성 모델을 내비게이션 레이어로 삼아 이기종 설비 텔레메트리를 통합 관제하는 디지털 트윈 UI.

    [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/mxd-twin/){ target="_blank" }

-   **3D Gaussian Splatting Viewer**

    ---

    브라우저에서 `.ply` 스플랫 씬을 실시간 렌더링하는 WebGL/3DGS 뷰어.

    [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/splatting-viewer/){ target="_blank" }

-   **EBS 영어 회화 추출 파이프라인 (Whisper)**

    ---

    라디오 자동 다운로드 → `faster-whisper` 전사 → 음악 구간 분리로 영어 대화만 추출해 웹 플레이어까지 자동 배포.

    [:octicons-arrow-right-24: 상세 아키텍처](projects/ebs-whisper-pipeline.md)

-   **myslide — 다크 테마 SVG 슬라이드 엔진**

    ---

    YAML 코드로 슬라이드를 선언하면 다크 테마 SVG 웹 뷰어와 PNG/PDF(Playwright)로 빌드하는 자체 프레젠테이션 엔진.

    [:octicons-link-external-16: GitHub 보기](https://github.com/leeyunhome/myslide){ target="_blank" }

</div>

[:octicons-arrow-right-24: 전체 개인 프로젝트 모아보기](projects/index.md)

---

## 기술 스택

| 영역 | 스택 |
|---|---|
| Edge SoC | NVIDIA Jetson Orin NX / Xavier · Hailo-15H · Eyenix EN675/EN683 · Raspberry Pi 4B |
| 추론 최적화 | TensorRT (FP16/INT8) · ONNX Runtime · PyTorch · DeepStream |
| 임베디드 · 시스템 | Embedded Linux · `perf` / `ftrace` · Docker · ROS/ROS2 |
| AI · 멀티미디어 | OpenAI Whisper (`faster-whisper`) · Gemini API · VLM/VLA |
| 3D · 시각화 | 3D Gaussian Splatting · WebGL / Three.js · SVG/Canvas |
| 운영·품질·문서 | Node-RED · SonarQube · SBOM · Jira · Confluence |
| 언어 | Python · C/C++ · JavaScript / TypeScript |

[:octicons-arrow-right-24: 전체 기술 역량 보기](skills.md)

---

<div style="text-align:center; margin-top:2em; color:var(--md-default-fg-color--light)">
<a href="https://leeyunhome.github.io/" target="_blank">프로젝트 허브 (24+ 앱)</a> &nbsp;|&nbsp;
<a href="https://github.com/leeyunhome" target="_blank">GitHub</a> &nbsp;|&nbsp;
<a href="about.md">프로필</a>
</div>
