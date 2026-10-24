# Intelligent Warehouse Object Detection — Project Report

## Objective
Demonstrate object detection on a warehouse image using pretrained YOLO11n.

## Methodology
The input image was processed using YOLO11n pretrained on COCO.
Predictions were generated at a confidence threshold of 0.25.

## Recorded Results
- Input image: ruchindra-gunasekara-GK8x_XCcDZg-unsplash.jpg
- Image dimensions: 3024 × 4032
- Number of detections: 0
- Inference time: 8.7212 seconds
- Execution device: 0

## Evaluation
The recorded inference time and detection counts describe this run only.
Precision, recall, and mAP have not been calculated because ground-truth
warehouse annotations were not provided.

## Limitations
The model is not specifically trained for warehouse equipment and may
not recognize all relevant objects.

## Conclusion
This project demonstrates a basic pretrained computer vision pipeline.
A warehouse-specific annotated dataset is needed for a rigorous evaluation.
