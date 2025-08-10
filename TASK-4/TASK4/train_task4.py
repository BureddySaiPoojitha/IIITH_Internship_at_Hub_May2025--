from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # you can also use yolov8s.pt
model.train(
    data="TASK4/data.yaml",
    epochs=25,
    imgsz=640
)
