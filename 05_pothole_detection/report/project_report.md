# Project Report: Pothole Detection

## Problem Statement
Road potholes can affect road safety and driving comfort.
Computer vision may help automate road-surface inspection.

## Objective
Demonstrate a basic image-processing pipeline on a road image.

## Methodology
A pretrained YOLO11n model processes the uploaded image and
returns its supported general-object predictions.

## Experimental Output
- Input image: input_road.jpg
- Model: YOLO11n pretrained on COCO
- General objects detected: 0

The annotated output is saved in ../results/road_detection.jpg.

## Evaluation
This run does not measure pothole-detection accuracy. The model
has no dedicated pothole class and no ground-truth annotations
were used. Precision, recall, and mAP are therefore not reported.

## Limitations and Future Work
Use a labelled pothole dataset, fine-tune an object detector,
and evaluate on a held-out test set before claiming pothole detection.
