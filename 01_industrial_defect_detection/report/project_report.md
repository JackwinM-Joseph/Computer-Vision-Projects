# Industrial Defect Detection Using YOLO11n

## Abstract
This project applies an object detection model to identify steel-surface
defects in industrial images.

## Objective
To detect and localize six defect classes using a fine-tuned YOLO11n model.

## Methodology
The dataset was obtained in YOLO format. A pretrained YOLO11n model was
fine-tuned using the training split and evaluated on the validation split.

## Results
- Precision: 65.54%
- Recall: 69.61%
- mAP@50: 73.61%
- mAP@50–95: 39.89%

The validation comprised 360 images and 830 annotated instances.

## Discussion
The model performed well on some classes, particularly scratches and
patches. Crazing showed lower detection performance. The results indicate
that further data collection, augmentation, and model tuning may improve
performance.

## Conclusion
The project demonstrates a practical computer vision pipeline for
industrial surface defect detection. Validation results are documented
along with the training curves and confusion matrix.

## Limitation
These metrics describe the recorded validation run, not an independent
test-set evaluation. Performance in real industrial environments requires
additional testing.
