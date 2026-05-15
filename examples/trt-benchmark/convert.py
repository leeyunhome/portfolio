"""YOLOv8n PyTorch -> ONNX -> TensorRT (FP32/FP16/INT8) 변환.

산출물:
    weights/yolov8n.pt
    weights/yolov8n.onnx
    weights/yolov8n_fp32.engine
    weights/yolov8n_fp16.engine
    weights/yolov8n_int8.engine
"""

import shutil
from pathlib import Path
from ultralytics import YOLO

WEIGHTS = Path(__file__).parent / "weights"
WEIGHTS.mkdir(exist_ok=True)


def main() -> None:
    # 모델 다운로드 (최초 1회)
    pt_path = WEIGHTS / "yolov8n.pt"
    if not pt_path.exists():
        YOLO("yolov8n.pt")
        src = Path("yolov8n.pt")
        if src.exists():
            shutil.move(str(src), str(pt_path))

    # ONNX
    print("[1/4] ONNX export")
    YOLO(str(pt_path)).export(format="onnx", imgsz=640, opset=12)

    # TensorRT FP32
    print("[2/4] TensorRT FP32 engine")
    fp32 = Path(YOLO(str(pt_path)).export(format="engine", imgsz=640))
    fp32.rename(WEIGHTS / "yolov8n_fp32.engine")

    # TensorRT FP16
    print("[3/4] TensorRT FP16 engine")
    fp16 = Path(YOLO(str(pt_path)).export(format="engine", imgsz=640, half=True))
    fp16.rename(WEIGHTS / "yolov8n_fp16.engine")

    # TensorRT INT8 (COCO128 캘리브레이션)
    print("[4/4] TensorRT INT8 engine (COCO128 calibration)")
    int8 = Path(YOLO(str(pt_path)).export(format="engine", imgsz=640, int8=True, data="coco128.yaml"))
    int8.rename(WEIGHTS / "yolov8n_int8.engine")

    print("\nDone — weights/")
    for p in sorted(WEIGHTS.iterdir()):
        print(f"  {p.name:35s} {p.stat().st_size / 1024 / 1024:8.2f} MB")


if __name__ == "__main__":
    main()
