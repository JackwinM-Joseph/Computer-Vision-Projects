# Vision-Based Waste Detection and Classification

## Problem Statement
Waste identification can support waste monitoring and segregation workflows.

## Objective
Demonstrate object detection on an image containing waste-related objects.

## Dataset
A user-provided image is used for the demonstration. The pretrained model
uses general-purpose COCO classes. See dataset/DATASET_INFO.md.

## Methodology
1. Upload an image.
2. Run YOLO11n detection.
3. Apply a confidence threshold of 0.25.
4. Save bounding boxes, classes, confidence scores, and annotated output.

## Tools
Python, Ultralytics YOLO, PyTorch, OpenCV, Pandas.

## Results
See results/detections.csv, results/run_statistics.csv, and
results/waste_detection.jpg.

## Performance Evaluation
Detection count, confidence scores, and inference time are recorded.
Precision, recall, and mAP are not reported because ground-truth annotations
were not supplied.

## Limitations
The pretrained model is not a waste-specific classifier. It cannot reliably
distinguish every waste material category.

## Conclusion
The project demonstrates a basic object detection pipeline. A waste-specific
dataset and trained model are required for dependable material classification.
