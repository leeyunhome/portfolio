# 기술 역량

> Edge AI 추론 최적화부터 임베디드 리눅스·하드웨어 제어, 양산 운영·보안, 그리고 풀스택 프로토타이핑까지의 보유 역량입니다.

---

## 1. 추론 엔진 최적화 (Inference Optimization)

| 역량 | 상세 | 수준 |
|---|---|---|
| ONNX 변환 | PyTorch → ONNX export, 연산자 호환성 검증 | ★★★★☆ |
| TensorRT 최적화 | FP32 / FP16 / INT8 변환·벤치마킹 | ★★★★☆ |
| 배치·스레딩·메모리 튜닝 | SoC 레지스터 레벨 메모리 접근 타이밍 최적화 포함 | ★★★★☆ |
| 성능 프로파일링 | 지연시간·FPS·메모리 사용량 정량 측정 | ★★★★☆ |
| 사이클타임 설계 | 라인 사이클타임 내 추론 완료 파이프라인 구성 | ★★★☆☆ |

---

## 2. Edge 배포 및 임베디드 리눅스 (Edge & Embedded Systems)

| 역량 | 상세 | 수준 |
|---|---|---|
| NVIDIA Jetson | Orin NX, Xavier — JetPack, DeepStream, cuDNN | ★★★★★ |
| Hailo | Hailo-15H NPU 모델 컴파일·추론 | ★★★★☆ |
| Eyenix SoC | EN675/EN683 — 레지스터 제어, ISP 파라미터 | ★★★★☆ |
| 커널 · 성능 분석 | Embedded Linux 커널 빌드, `perf` / `ftrace` 병목 프로파일링 | ★★★★☆ |
| Docker | 컨테이너 패키징, GPU 리소스 할당, 이미지 관리 | ★★★★☆ |
| ROS/ROS2 | 센서 데이터(IMU, ADC, CAN) 동기화, 노드 설계 | ★★★☆☆ |

---

## 3. 시스템 신뢰성 및 운영 (Operations & Reliability)

| 역량 | 상세 | 수준 |
|---|---|---|
| 에이징 테스트 | CPU/GPU Full-load 93일 연속 가동, 가동률 100% 달성 | ★★★★★ |
| Memory Leak 탐지 | 장기 가동 환경에서의 메모리 누수 프로파일링·조치 | ★★★★☆ |
| 발열 관리 | 챔버 환경 열 프로파일링, 쿨링 설계 검증 | ★★★★☆ |
| SOP 수립 | 장애 대응 절차 문서화, 유지보수 체크리스트 | ★★★★☆ |
| 모니터링 | Node-RED 기반 실시간 대시보드 구성 | ★★★☆☆ |
| 로그/알람 체계 | 장애 수준별 알람 설계, 이슈 트래킹(Jira) | ★★★☆☆ |

---

## 4. 비전 AI · 멀티모달 · 서비스 파이프라인

| 역량 | 상세 | 수준 |
|---|---|---|
| YOLO (v5/v7/v8) | 검출·분류 모델 학습, Edge 최적화 | ★★★★☆ |
| LPR | 번호판 인식 파이프라인 설계 및 배포 | ★★★★☆ |
| VLM/VLA | Jetson Orin NX 기반 멀티모달 추론 검증 | ★★★☆☆ |
| 오검출 방지 | 임계값 조정, ROI 설정, 데이터 파손 원인 분석 | ★★★★☆ |
| 음성 · LLM 파이프라인 | `faster-whisper` ASR, Gemini API, 자동 수집·배포 파이프라인 | ★★★★☆ |
| 3D · 디지털 트윈 | 3D Gaussian Splatting, WebGL, 3D 공간 관제 UI | ★★★☆☆ |

---

## 5. SW 품질 및 보안 (Quality & Security)

| 역량 | 상세 | 수준 |
|---|---|---|
| 정적 분석 | SonarQube, Cppcheck — 코드 품질 게이트 운영 | ★★★★☆ |
| SBOM | 소프트웨어 자재명세서 생성 및 관리 | ★★★☆☆ |
| 보안 인증 대응 | 국방·공공 보안 인증 규격 준수 | ★★★☆☆ |
| 기술 문서화 | AI SDK 영문 문서 작성, 배포 서비스 구축 | ★★★★☆ |

---

## 핵심 문제 해결 역량 요약

| 영역 | 보유 경험 |
|---|---|
| 추론 최적화 & 양자화 | PyTorch → ONNX → TensorRT(FP16/INT8) Jetson·Hailo·Eyenix 적용·검증 |
| 컨테이너 배포 & 런타임 | Edge SoC 환경 Docker 패키징 및 GPU 리소스 할당 |
| 성능 프로파일링 & 사이클타임 | 라인 투입 전 정량 벤치마킹, `perf`/`ftrace` 계측, 파이프라인 병렬화 |
| 모니터링 & 장애 대응(RCA) | Node-RED 대시보드, Jira 트래킹, 93일 에이징 기반 Root Cause 분석 |
| 표준 운영 문서(SOP) | 양산 현장 투입용 SOP 및 유지보수 체크리스트 직접 작성 |
| 보안 & 품질 관리 | SonarQube·SBOM·국방/공공 보안 인증 대응 |
| 개발 언어 | Python · C/C++ · JavaScript / TypeScript |
