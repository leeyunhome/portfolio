# 이윤호 · Applied AI / Embedded SW Engineer

<div style="font-size:1.15em; margin:0.8em 0 2em; line-height:1.7; color:var(--md-default-fg-color--light)">
SoC 레지스터부터 현장 라인 사이클까지 —<br>
<strong>하드웨어와 소프트웨어를 넘나들어 제조 현장의 AI 추론 엔진을 배포·운영하는 엔지니어.</strong>
</div>

Edge SoC(Jetson, Hailo, Eyenix) 기반 비전 AI 시스템 배포 및 운영 경험 약 3년.
ONNX/TensorRT 추론 최적화, SoC 레지스터 레벨 디버깅, 93일 무중단 에이징 테스트, VLM/VLA 선행 연구까지 —
AI 파이프라인의 하드웨어 레이어부터 운영 SOP까지 전 스택을 직접 다뤄왔습니다.

---

## 핵심 프로젝트

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
    국방·공공(STQC, KISA) 인증 기반 마련.

    [:octicons-arrow-right-24: 자세히 보기](cases/04-sw-quality.md)

-   **TensorRT 정밀도 벤치마크 — 실행 가능한 데모**

    ---

    PyTorch → ONNX → TensorRT(FP32/FP16/INT8) 변환 및 지연시간/FPS 측정.
    RTX 4060 환경에서 직접 재현 가능한 코드 포함.

    [:octicons-arrow-right-24: 자세히 보기](cases/05-trt-benchmark.md)

</div>

---

## 기술 스택

| 영역 | 스택 |
|---|---|
| Edge SoC | NVIDIA Jetson Orin NX / Xavier · Hailo-15H · Eyenix EN675/EN683 |
| 추론 최적화 | TensorRT (FP16/INT8) · ONNX Runtime · PyTorch |
| 배포 | Docker · ROS/ROS2 |
| 운영·모니터링 | Node-RED · SonarQube · Jira · Confluence |
| 언어 | Python · C/C++ |

[:octicons-arrow-right-24: 전체 기술 역량 보기](skills.md)

---

<div style="text-align:center; margin-top:2em; color:var(--md-default-fg-color--light)">
<a href="https://github.com/leeyunhome" target="_blank">GitHub</a> &nbsp;|&nbsp;
<a href="about.md">프로필</a>
</div>
