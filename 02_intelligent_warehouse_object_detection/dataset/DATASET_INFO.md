# Dataset and Model Information

## Input data
This demonstration uses a user-provided warehouse image.
The image filename is recorded in results/run_statistics.csv.

## Model
Ultralytics YOLO11n pretrained on the COCO dataset.
Model weights are downloaded automatically when the source code runs.

## Dataset source
COCO dataset: https://cocodataset.org/

## Important limitation
This is pretrained general-purpose object detection, not a warehouse-specific
model trained on warehouse annotations. It can detect only classes supported
by the pretrained model. It may not recognize pallets, forklifts, or packages
as dedicated classes.

No custom warehouse training or independent test-set evaluation was performed.
