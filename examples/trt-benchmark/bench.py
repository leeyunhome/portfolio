"""TensorRT 엔진별 추론 지연시간/처리량 벤치마크.

각 precision 별로 warmup 50회 후 1000회 추론 → mean/p50/p99 지연시간 + FPS.
출력: benchmark.md (Markdown 표), benchmark.csv
"""

from pathlib import Path
import time
import numpy as np
import pandas as pd
from ultralytics import YOLO

WEIGHTS = Path(__file__).parent / "weights"
OUT = Path(__file__).parent

PRECISIONS = {
    "FP32": WEIGHTS / "yolov8n_fp32.engine",
    "FP16": WEIGHTS / "yolov8n_fp16.engine",
    "INT8": WEIGHTS / "yolov8n_int8.engine",
}

WARMUP = 50
ITERS = 1000
IMG = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)


def bench_one(name: str, engine_path: Path) -> dict:
    print(f"[{name}] loading {engine_path.name}")
    model = YOLO(str(engine_path))

    for _ in range(WARMUP):
        model.predict(IMG, verbose=False, device=0)

    latencies = []
    for _ in range(ITERS):
        t = time.perf_counter()
        model.predict(IMG, verbose=False, device=0)
        latencies.append((time.perf_counter() - t) * 1000.0)

    arr = np.asarray(latencies)
    size_mb = engine_path.stat().st_size / 1024 / 1024
    return {
        "precision": name,
        "engine_size_mb": round(size_mb, 2),
        "mean_ms": round(arr.mean(), 3),
        "p50_ms": round(np.percentile(arr, 50), 3),
        "p99_ms": round(np.percentile(arr, 99), 3),
        "fps": round(1000.0 / arr.mean(), 1),
    }


def main() -> None:
    rows = []
    for name, path in PRECISIONS.items():
        if not path.exists():
            print(f"[{name}] SKIP — {path} not found. Run convert.py first.")
            continue
        rows.append(bench_one(name, path))

    df = pd.DataFrame(rows)
    print("\n" + df.to_string(index=False))

    (OUT / "benchmark.csv").write_text(df.to_csv(index=False), encoding="utf-8")
    (OUT / "benchmark.md").write_text(df.to_markdown(index=False), encoding="utf-8")
    print(f"\nWrote: {OUT / 'benchmark.csv'}\n       {OUT / 'benchmark.md'}")


if __name__ == "__main__":
    main()
