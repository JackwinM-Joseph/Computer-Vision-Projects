# Pothole Detection Using Computer Vision

## Objective
Explore a computer-vision pipeline using a road image.

## Current Implementation
This version runs pretrained YOLO11n for general object detection.
It is not a pothole-specific detector.

## Run
Install packages with: pip install -r requirements.txt
Then run:
python src/detect.py --image dataset/input_road.jpg --output results/road_detection.jpg

## Outputs
- results/road_detection.jpg
- results/detections.csv
- results/run_statistics.csv

## Limitations
The pretrained COCO model has no dedicated pothole class.
A pothole-labelled dataset and model fine-tuning are required
for a genuine pothole-detection project.
No pothole accuracy or mAP is claimed.
