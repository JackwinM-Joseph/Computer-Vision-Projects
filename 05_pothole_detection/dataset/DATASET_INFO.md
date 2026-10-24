# Dataset Information

This demonstration uses a user-uploaded road image.
The model is pretrained YOLO11n using the COCO dataset.

Important: COCO does not provide a dedicated pothole class.
Therefore, this code does not validate pothole detection.

For actual pothole detection, use a labelled pothole dataset
and train or fine-tune an object detector on pothole annotations.
Evaluate using ground-truth labels before reporting precision,
recall, or mean Average Precision (mAP).
