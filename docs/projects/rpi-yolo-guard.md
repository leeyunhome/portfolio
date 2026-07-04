# Raspberry Pi + YOLO 홈 감시 카메라

> 남는 라즈베리 파이를 현관 감시 카메라로 — YOLOv8n을 실사용 가능한 수준까지 최적화한 기록.

---

## 배경

집에 굴러다니던 Raspberry Pi 4B(4GB)와 USB 웹캠이 있었다.
현관에 달아서 사람이 나타나면 알림을 보내는 걸 만들어 보고 싶었다.

---

## 첫 시도: YOLOv8n PyTorch

```
환경: RPi 4B · Python 3.11 · ultralytics
결과: ~3 FPS · CPU 온도 85°C · 실사용 불가
```

예상은 했지만, 3 FPS에서 온도가 85도까지 올라가니 장시간 운영이 불가능했다.

---

## 최적화 경로

### 1단계 — NCNN 변환

YOLOv8n → ONNX → NCNN 변환 후 ARM Cortex-A72에 맞게 스레드 수 조정.

```bash
# ONNX export
yolo export model=yolov8n.pt format=onnx imgsz=320

# NCNN 변환 (onnx2ncnn)
onnx2ncnn yolov8n.onnx yolov8n.param yolov8n.bin
```

### 2단계 — 입력 해상도 조정

640×640 → 320×320으로 낮춤. 사람 감지 정확도는 현관 거리에서 충분.

### 3단계 — 프레임 건너뛰기

매 프레임 추론 → 2프레임 간격 추론. 침입 감지 목적엔 1초에 한 번도 충분.

---

## 결과

| | PyTorch (원본) | NCNN (최적화) |
|---|---|---|
| FPS | ~3 | ~12 |
| CPU 온도 | 85°C | 62°C |
| 사람 감지율 (현관 5m) | 91% | 89% |

---

## 알림 연동

Python + Telegram Bot API로 사람이 감지되면 스냅샷 전송.
오탐(나뭇잎·고양이) 방지를 위해 confidence 0.6 이상 + 3프레임 연속 감지 조건 추가.

```python
if confidence > 0.6 and consecutive_frames >= 3:
    bot.send_photo(chat_id=CHAT_ID, photo=open(snapshot_path, 'rb'))
```

---

## 느낀 점

회사에서 Jetson·Hailo 같은 전용 하드웨어에 TensorRT/HailoRT로 최적화하는 게 얼마나 편한 환경인지 새삼 느꼈다.
범용 SBC에서 모델을 돌리려면 변환 체인 하나하나가 전부 수작업이다.

NCNN은 문서가 적고 레이어 지원이 불안정해서, 변환 실패 시 원인 파악이 힘들었다.
다음엔 OpenVINO + Intel NCS2 조합을 시도해 볼 예정.
