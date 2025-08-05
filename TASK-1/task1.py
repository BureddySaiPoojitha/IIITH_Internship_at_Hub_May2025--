from ultralytics import YOLO
import cv2

# Load pretrained YOLOv8 segmentation model
model = YOLO("yolov8n-seg.pt")  # Use 'yolov8n-seg.pt' for lightweight segmentation

# Load image
img_path = "bus.jpg"
results = model(img_path, save=True, imgsz=640)

# Show segmented results
for r in results:
    r.show()
