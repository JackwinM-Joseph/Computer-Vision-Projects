# Project Report: Animal Detection for Smart Agriculture

## Problem Statement
Manual animal monitoring can be time-consuming. Computer vision can
support automated monitoring by detecting animals in images.

## Objective
Detect supported animal classes using a pretrained object detector.

## Implementation
YOLO11n processes the uploaded image and predicts classes, bounding
boxes and confidence scores. The annotated image and CSV are saved.

## Experimental Results
- Input: input_animal.jpg
- Model: YOLO11n pretrained on COCO
- Confidence threshold: 0.25
- Objects detected: 1

See ../results/detections.csv for prediction details.

## Performance Evaluation
The number of detections is not an accuracy metric. Precision, recall
and mAP are not reported because ground-truth annotations were not used.

## Limitations
This is a sample demonstration, not a validated agricultural system.
Results depend on supported classes, lighting, viewpoint and image quality.

## Conclusion
The project demonstrates a basic image-based animal detection pipeline.
