from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser(description='Animal Detection')
parser.add_argument('--image', required=True)
parser.add_argument('--output', default='animal_detection.jpg')
parser.add_argument('--confidence', type=float, default=0.25)
args = parser.parse_args()

model = YOLO('yolo11n.pt')
result = model.predict(source=args.image, conf=args.confidence, verbose=False)[0]
result.save(filename=args.output)
print('Objects detected:', len(result.boxes))
for box in result.boxes:
    class_id = int(box.cls[0].item())
    confidence = float(box.conf[0].item())
    print(model.names[class_id], round(confidence, 3))
