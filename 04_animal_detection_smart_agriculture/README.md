# Animal Detection for Smart Agriculture

## Objective
Demonstrate image-based animal detection using a pretrained YOLO model.

## Method
1. Upload an animal image.
2. Run YOLO11n object detection.
3. Save bounding boxes, class names and confidence scores.

## Project Structure
- src/detect.py: runnable source code
- dataset/: input image and dataset information
- results/: annotated image and CSV files
- screenshots/: input and output examples
- report/: project report

## Run locally
Install dependencies using: pip install -r requirements.txt
Then run:
python src/detect.py --image dataset/input_animal.jpg --output results/animal_detection.jpg

## Limitations
This model is pretrained on COCO and is not fine-tuned for agriculture.
No precision, recall or mAP is claimed without labelled evaluation data.
