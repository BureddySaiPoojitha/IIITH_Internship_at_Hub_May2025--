**Task 1 – YOLOv8 Setup & Image Segmentation**

## Objective
- Set up a Python virtual environment
- Install Ultralytics YOLOv8
- Test object detection and segmentation on a sample image (`bus.jpg`)

## Model Used
- `yolov8n-seg.pt` – Pretrained YOLOv8 model with segmentation head

## Input Image
- `bus.jpg` – Sample image downloaded from Ultralytics
  - Source: https://ultralytics.com/images/bus.jpg

## Output
- Detected objects (bus, people, vehicles) with class labels
- Segmentation masks overlayed on each object
- Output image saved to: `runs/segment/predict/bus.jpg`

## How to Run

1. **Create and activate a virtual environment**
```bash
python -m venv yolov8_env
yolov8_env\Scripts\activate

2. **Install YOLOv8**

```bash
pip install ultralytics

3. **Run the Script**

```bash
python task1.py
