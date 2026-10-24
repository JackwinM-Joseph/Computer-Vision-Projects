# Intelligent Warehouse Object Detection

## Problem Statement
Warehouses contain people and objects that may need to be identified
for inventory monitoring and operational awareness.

## Objective
Demonstrate image-based object detection in a warehouse scene using
a pretrained YOLO model.

## Dataset
A user-provided warehouse image is used for the demonstration.
Model: YOLO11n pretrained on COCO.
See `dataset/DATASET_INFO.md`.

## Methodology
1. Load the image.
2. Run YOLO object detection.
3. Filter detections using a confidence threshold of 0.25.
4. Draw bounding boxes and class labels.
5. Save detection records and inference statistics.

## Tools and Libraries
- Python
- Ultralytics YOLO
- PyTorch
- OpenCV
- Pandas

## Results
- Annotated image: `results/warehouse_detection.jpg`
- Detection table: `results/detections.csv`
- Runtime statistics: `results/run_statistics.csv`
- Screenshots: `screenshots/`

Actual detection counts and runtime are recorded by the program.

## Performance Evaluation
This demonstration records inference time, number of detections, classes,
and confidence scores. Precision, recall, and mAP require ground-truth
annotations and are not claimed by this pretrained-only demonstration.

## Limitations
The model is pretrained on general-purpose COCO classes and has not been
fine-tuned for warehouse-specific objects. It may miss forklifts, pallets,
packages, or other warehouse equipment.

## Conclusion
The project demonstrates a reusable object-detection pipeline for images.
Warehouse-specific training and annotated test data are needed for a
reliable warehouse monitoring system.

## How to Run
Install dependencies:

    pip install -r requirements.txt

Run:

    python src/detect.py --source path/to/warehouse.jpg
