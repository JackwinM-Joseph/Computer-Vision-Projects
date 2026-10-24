
from ultralytics import YOLO
import cv2
import time
import argparse
import pandas as pd
import torch
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--source", required=True, help="Image or video path")
parser.add_argument("--output", default="results")
args = parser.parse_args()

out = Path(args.output)
out.mkdir(parents=True, exist_ok=True)

model = YOLO("yolo11n.pt")
device = 0 if torch.cuda.is_available() else "cpu"

start = time.perf_counter()
results = model.predict(
    source=args.source,
    conf=0.25,
    device=device,
    verbose=False
)
elapsed = time.perf_counter() - start

rows = []
for result in results:
    result.save(filename=str(out / "detection_output.jpg"))
    for box in result.boxes:
        class_id = int(box.cls.item())
        rows.append({
            "class_name": model.names[class_id],
            "confidence": float(box.conf.item()),
            "xyxy": box.xyxy[0].tolist()
        })

pd.DataFrame(rows).to_csv(out / "detections.csv", index=False)
print("Detections:", len(rows))
print("Elapsed seconds:", round(elapsed, 4))
print("Device:", device)
