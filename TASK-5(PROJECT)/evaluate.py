from ultralytics import YOLO
import os

model = YOLO("runs/detect/safety_detection/weights/best.pt")

test_dir = "dataset/valid/images"
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)

for img in os.listdir(test_dir):
    if img.lower().endswith((".jpg", ".png", ".jpeg")):
        model.predict(
            source=os.path.join(test_dir, img),
            save=True,
            project=results_dir,
            name="outputs"
        )
