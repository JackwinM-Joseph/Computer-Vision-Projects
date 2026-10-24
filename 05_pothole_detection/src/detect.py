from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser(description='Road Object Detection Demo')
parser.add_argument('--image', required=True)
parser.add_argument('--output', default='road_detection.jpg')
parser.add_argument('--confidence', type=float, default=0.25)
args = parser.parse_args()

# COCO-pretrained YOLO does not have a dedicated pothole class.
model = YOLO('yolo11n.pt')
result = model.predict(source=args.image, conf=args.confidence, verbose=False)[0]
result.save(filename=args.output)
print('General objects detected:', len(result.boxes))
for box in result.boxes:
    class_id = int(box.cls[0].item())
    confidence = float(box.conf[0].item())
    print(model.names[class_id], round(confidence, 3))
