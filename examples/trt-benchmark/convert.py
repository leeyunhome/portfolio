"""YOLOv8n PyTorch -> ONNX -> TensorRT (FP32/FP16/INT8) 변환.

산출물:
    weights/yolov8n.pt        (PyTorch, ultralytics 자동 다운로드)
    weights/yolov8n.onnx      (ONNX)
    weights/yolov8n.engine    (TensorRT FP32)
    weights/yolov8n_fp16.engine
    weights/yolov8n_int8.engine
"""

from pathlib import Path
import shutil
from ultralytics import YOLO

WEIGHTS = Path(__file__).parent / "weights"
WEIGHTS.mkdir(exist_ok=True)


def _move_artifact(src_name: str, dst_name: str) -> None:
    src = Path(src_name)
    if src.exists():
        shutil.move(str(src), str(WEIGHTS / dst_name))


def main() -> None:
    pt_path = WEIGHTS / "yolov8n.pt"
    if not pt_path.exists():
        YOLO("yolov8n.pt")
        _move_artifact("yolov8n.pt", "yolov8n.pt")

    model = YOLO(str(pt_path))

    print("[1/4] ONNX export")
    model.export(format="onnx", imgsz=640, opset=12)
    _move_artifact(str(WEIGHTS / ".." / "yolov8n.onnx"), "yolov8n.onnx")

    print("[2/4] TensorRT FP32 engine")
    model.export(format="engine", imgsz=640)
    _move_artifact(str(WEIGHTS / ".." / "yolov8n.engine"), "yolov8n_fp32.engine")

    print("[3/4] TensorRT FP16 engine")
    model.export(format="engine", imgsz=640, half=True)
    _move_artifact(str(WEIGHTS / ".." / "yolov8n.engine"), "yolov8n_fp16.engine")

    print("[4/4] TensorRT INT8 engine (COCO128 캘리브레이션)")
    model.export(format="engine", imgsz=640, int8=True, data="coco128.yaml")
    _move_artifact(str(WEIGHTS / ".." / "yolov8n.engine"), "yolov8n_int8.engine")

    print("\nDone. weights/ 내용:")
    for p in sorted(WEIGHTS.iterdir()):
        print(f"  {p.name}  ({p.stat().st_size / 1024 / 1024:.2f} MB)")


if __name__ == "__main__":
    main()
