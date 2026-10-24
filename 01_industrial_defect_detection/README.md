# Industrial Defect Detection System Using YOLO

## 1. Problem Statement
Industrial steel surfaces may contain defects that reduce product quality.
Manual inspection can be time-consuming and inconsistent.

## 2. Objective
Develop an object detection model that identifies and localizes steel-surface
defects in images.

## 3. Dataset
Dataset: NEU Surface Defect Dataset
Source: https://universe.roboflow.com/neudefectdetection/neu-surface-defect-pohqa

The downloaded dataset contains training, validation, and test splits.
Six defect classes are used:
- Crazing
- Inclusion
- Patches
- Pitted surface
- Rolled-in scale
- Scratches

See dataset/DATASET_INFO.md for details.

## 4. Methodology
1. Load the annotated dataset in YOLO format.
2. Initialize the pretrained YOLO11n model.
3. Fine-tune the model on the training images.
4. Evaluate the model on the validation split.
5. Generate predictions and visualization plots.

## 5. Tools and Libraries
- Python
- Ultralytics YOLO11n
- PyTorch
- OpenCV
- NumPy
- Matplotlib

## 6. Validation Results
Results from the recorded validation run:

| Metric | Value |
|---|---:|
| Precision | 65.54% |
| Recall | 69.61% |
| mAP@50 | 73.61% |
| mAP@50–95 | 39.89% |

Validation split: 360 images, 830 annotated instances.

## 7. Results
Training curves, confusion matrices, and sample visualizations are included
in the results/ and screenshots/ directories.

## 8. Limitations
Performance varies by defect class. Crazing and rolled-in scale were more
challenging than scratches and patches. Results may also be affected by
lighting, image quality, dataset size, and the similarity between training
and real-world samples.

## 9. Conclusion
The project demonstrates YOLO-based detection and localization of six
steel-surface defect categories. The recorded validation results show
promising detection performance, while precise localization and weaker
classes remain areas for improvement.

## 10. How to Run
Install dependencies:

    pip install -r requirements.txt

Run inference on an image using the trained weights:

    yolo predict model=results/best.pt source=path/to/image.jpg
