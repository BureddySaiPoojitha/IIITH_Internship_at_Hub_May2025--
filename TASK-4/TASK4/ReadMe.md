# YOLOv8 Custom Object Detection - Task 4

## Overview
This project implements a custom object detection pipeline using Ultralytics YOLOv8.  
It includes dataset preparation, interactive bounding box labeling, and training on a custom card dataset with 5 classes:  
`ace`,`number`, `jack`, `queen`, `king`, and `joker`.

## Dataset Structure
TASK4/
│
|─ images/
│ |─ train/ # Training images (.jpg, .png, .jpeg)
│ |─ valid/ # Validation images
│
|─ labels/
│ |─ train/ # YOLO-format label files (.txt)
│ |─ valid/
│
|─ label_bounding_boxes.py # Interactive labeling tool using OpenCV
|─ data.yaml # Dataset config file for YOLOv8 training
|─ train_yolo.py # Script or commands to launch training (optional)



## Setup Instructions
1. Install dependencies:
   ```bash
   pip install ultralytics opencv-python
Label images (if not done):


python label_bounding_boxes.py
Draw bounding boxes interactively and save labels.

Verify data.yaml paths and classes.

Train YOLOv8:

yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 batch=16

Class Names:

ace

number

jack

queen

king

joker