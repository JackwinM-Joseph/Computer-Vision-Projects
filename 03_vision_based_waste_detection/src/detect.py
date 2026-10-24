from ultralytics import YOLO
import argparse
import torch
from pathlib import Path
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--source", required=True)
parser.add_argument("--output", default="results")
args = parser.parse_args()

out = Path(args.output)
out.mkdir(parents=True, exist_ok=True)
model = YOLO("yolo11n.pt")
device = 0 if torch.cuda.is_available() else "cpu"
results = model.predict(args.source, conf=0.25, device=device)

rows = []
for result in results:
    result.save(filename=str(out / "detection.jpg"))
    for box in result.boxes:
        cid = int(box.cls.item())
        rows.append({
            "class": model.names[cid],
            "confidence": float(box.conf.item())
        })
pd.DataFrame(rows).to_csv(out / "detections.csv", index=False)
print("Detections:", len(rows))
