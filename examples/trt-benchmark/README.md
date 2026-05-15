# TensorRT Precision Benchmark (YOLOv8n)

PyTorch → ONNX → TensorRT (FP32 / FP16 / INT8) 변환 및 벤치마크 데모.

> **방법론 검증용 데모**입니다. 실측 환경은 데스크탑 GPU(RTX 4060)이며,
> Edge(Jetson) 또는 서버 GPU와 절대 지연시간은 다릅니다. FP32 → FP16 → INT8 의
> 상대 가속비와 정확도 트레이드오프는 동일한 패턴을 보입니다.

## 환경

- Windows 11 / Python 3.11 (conda)
- NVIDIA RTX 4060 Laptop · CUDA 13.0 · TensorRT 10.x

## 실행

```powershell
conda create -n trtbench python=3.11 -y
conda activate trtbench
pip install -r requirements.txt

python convert.py    # 모델 다운로드 + ONNX/TensorRT 엔진 생성
python bench.py      # 지연시간/처리량 측정 → benchmark.md
```

## 산출물

- `weights/yolov8n.pt|onnx|*.engine` — 변환 단계별 모델
- `benchmark.md`, `benchmark.csv` — 측정 결과표

## INT8 캘리브레이션

Ultralytics가 내부적으로 `IInt8EntropyCalibrator2` 를 사용해 COCO128(128장) 으로
양자화 스케일을 자동 결정합니다. 실제 양산에서는 **현장 분포를 대표하는 200~500장**
캘리브레이션 셋이 권장됩니다.
