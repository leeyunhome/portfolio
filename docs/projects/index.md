# 개인 프로젝트 (Personal Projects)

업무 외 시간에 직접 설계·구현·배포한 프로젝트들입니다.
임베디드/AI 최적화 실험부터 3D 그래픽스, 실시간 모니터링, 브라우저 유틸리티까지 모든 라이브 데모는 [프로젝트 허브(leeyunhome.github.io)](https://leeyunhome.github.io/)에서도 바로 실행할 수 있습니다.

---

=== "AI · 딥러닝"

    <div class="grid cards" markdown>

    -   **EBS 영어 회화 추출 파이프라인** · Whisper ASR

        ---

        EBS 라디오 자동 다운로드 → `faster-whisper`(`large-v3-turbo`) 전사 → `inaSpeechSegmenter` 음악 구간 분리 → 웹 플레이어 자동 배포.

        [:octicons-arrow-right-24: 상세 아키텍처](ebs-whisper-pipeline.md) · [:octicons-link-external-16: 웹 앱](https://leeyunhome.github.io/ebs-learning/){ target="_blank" }

    -   **굿모닝 팝스 팟캐스트 파이프라인** · Whisper ASR

        ---

        KBS 굿모닝 팝스 라디오를 자동 수집·전사하고 코너별로 추출·최적화해 모바일 친화 웹 플레이어로 배포.

        [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/goodmorningpops_podcast/index.html){ target="_blank" }

    -   **Jetson MLOps Lab** · 비전 파이프라인 최적화

        ---

        Jetson Orin 환경에서 비전 추론 파이프라인의 정밀도·지연시간·처리량을 벤치마킹하고 문서화한 MLOps 실험실.

        [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/jetson-mlops-lab/){ target="_blank" }

    -   **Deep Learning Portfolio & VGG19 전이학습**

        ---

        `nn.Module` 기반 선형회귀·autograd 계산 그래프 시각화(`torchviz`), SGD vs Adam 비교, CIFAR-10 VGG19 전이학습 노트북.

        [:octicons-link-external-16: DL Portfolio](https://leeyunhome.github.io/deep-learning-portfolio/){ target="_blank" } · [:octicons-link-external-16: VGG19](https://leeyunhome.github.io/dl-portfolio/){ target="_blank" }

    -   **AI 챗봇 & 글씨 교정 연습** · Gemini

        ---

        별도 로그인 없이 API 키만으로 쓰는 한국어 Gemini 챗봇과, 손글씨 교정을 돕는 AI 웹 앱.

        [:octicons-link-external-16: AI 챗봇](https://leeyunhome.github.io/ai_chatbot_hodu_ai/){ target="_blank" } · [:octicons-link-external-16: 글씨 교정](https://leeyunhome.github.io/writing-coach/){ target="_blank" }

    </div>

=== "임베디드 · 모니터링"

    <div class="grid cards" markdown>

    -   **perf/ftrace 성능 프로파일링 — Jetson Orin**

        ---

        Linux `perf`와 `ftrace`를 활용해 Jetson Orin의 커널 스케줄링 및 연산 병목을 계측·분석한 리포트.

        [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/jetson-perf-profiling/){ target="_blank" }

    -   **임베디드 리눅스 테스트 자동화**

        ---

        디바이스 팜 기반 임베디드 리눅스 타깃 자동 검증 및 회귀 테스트 파이프라인 포트폴리오.

        [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/automation-portfolio/){ target="_blank" }

    -   **리눅스 커널 빌드 & ftrace 실습 — Raspberry Pi 4B**

        ---

        Raspberry Pi 4B 타깃 커널 크로스 컴파일, 부팅/모듈 검증, `ftrace` 트레이싱 실습 저장소.

        [:octicons-link-external-16: GitHub 보기](https://github.com/leeyunhome/rpi-kernel-lab){ target="_blank" }

    -   **Edge Monitor & StockPulse** · 실시간 모니터링

        ---

        엣지 디바이스 플릿 관제 UI(`Edge Monitor`)와 실시간 시세/지표 모니터링 대시보드(`StockPulse`).

        [:octicons-link-external-16: Edge Monitor](https://leeyunhome.github.io/edge-monitor/){ target="_blank" } · [:octicons-link-external-16: StockPulse](https://leeyunhome.github.io/SmartStock-AI/){ target="_blank" }

    </div>

=== "3D 그래픽스 · 디지털 트윈"

    <div class="grid cards" markdown>

    -   **mxd-twin — 복합단지 통합관제** · 디지털 트윈

        ---

        3DGS 기반 공간 재구성 모델을 인터페이스로 삼아 이기종 설비 텔레메트리를 통합 관제하는 디지털 트윈.

        [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/mxd-twin/){ target="_blank" }

    -   **3D Gaussian Splatting Viewer & Field2Scene**

        ---

        웹 브라우저용 3DGS 실시간 뷰어와, 현장 데이터 기반 3D 씬 재구성 파이프라인(`Field2Scene`).

        [:octicons-link-external-16: 3DGS Viewer](https://leeyunhome.github.io/splatting-viewer/){ target="_blank" } · [:octicons-link-external-16: Field2Scene](https://github.com/leeyunhome/field2scene){ target="_blank" }

    -   **Cloth Lab & 3D Lounge**

        ---

        실시간 의상 물리 시뮬레이션(`Cloth Lab`)과 다중 접속 3D 웹 라운지(`Lounge`).

        [:octicons-link-external-16: Cloth Lab](https://leeyunhome.github.io/cloth-simulation/){ target="_blank" } · [:octicons-link-external-16: 3D Lounge](https://lounge.mszeta.workers.dev/){ target="_blank" }

    </div>

=== "도구 · 시각화"

    <div class="grid cards" markdown>

    -   **myslide — 다크 테마 슬라이드 엔진**

        ---

        YAML 선언형 코드로 다크 테마 SVG 슬라이드(11종 다이어그램 컴포넌트 포함)와 PNG/PDF를 생성하는 자체 엔진.

        [:octicons-link-external-16: GitHub 보기](https://github.com/leeyunhome/myslide){ target="_blank" }

    -   **Data Visualization Playbook**

        ---

        히스토그램·KDE 비교 등 데이터 분석·시각화 기법을 인터랙티브하게 정리한 플레이북.

        [:octicons-link-external-16: 라이브 보기](https://leeyunhome.github.io/data-visualization-playbook/){ target="_blank" }

    -   **브라우저 로컬 유틸리티 모음**

        ---

        서버 전송 없이 브라우저에서 처리하는 이미지 리사이저, PDF 병합/분리, 글자수 세기, 박자 연습 등 미니 앱들.

        [:octicons-link-external-16: Image Resizer](https://leeyunhome.github.io/Smart-Image-Resizer/){ target="_blank" } · [:octicons-link-external-16: PDF Tool](https://leeyunhome.github.io/pdf-merger/){ target="_blank" } · [:octicons-link-external-16: 박자 연습](https://leeyunhome.github.io/apps/rhythm-practice/){ target="_blank" }

    </div>
