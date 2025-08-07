from ultralytics import YOLO
import cv2
import os

model = YOLO("yolov8n.pt")  # or yolov8s.pt for more accuracy

input_folder = "frames"
output_folder = "detected_frames"
os.makedirs(output_folder, exist_ok=True)

for frame in sorted(os.listdir(input_folder)):
    img_path = os.path.join(input_folder, frame)
    result = model(img_path)[0]
    annotated = result.plot()
    cv2.imwrite(os.path.join(output_folder, frame), annotated)

print("Detection complete.")
