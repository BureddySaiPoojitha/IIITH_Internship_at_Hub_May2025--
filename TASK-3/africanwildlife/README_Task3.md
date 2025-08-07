# Task 3: Training YOLOv8 on African Wildlife Dataset

## Objective  
Train and evaluate a YOLOv8 object detection model on the **African Wildlife dataset**, featuring 4 animal classes:  
`buffalo`, `elephant`, `rhino`, `zebra`.

---

## Dataset Structure

Organized into the YOLO format:

```
TASK-3/africanwildlife/
|── train/
|   |── images/
|   |── labels/
|── val/
|   |── images/
|   |── labels/
|── test/
    |── images/
    |── labels/
```

Each `.txt` file in `labels/` contains bounding box annotations in YOLO format:  
`<class_id> <x_center> <y_center> <width> <height>` (normalized).

---

## Configuration

### `data.yaml`
```yaml
path: TASK-3/africanwildlife
train: train/images
val: val/images
test: test/images

nc: 4
names: ['buffalo', 'elephant', 'rhino', 'zebra']
```

---

## Training

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=25 imgsz=640
```

---

## Results & Evaluation

YOLOv8 generates results in the `runs/detect/train/` directory.

### Key Outputs:
- `confusion_matrix.png` – visualize true vs predicted class accuracy.
- `results.png` – training metrics: precision, recall, mAP50, and loss curves.

If **no curves/metrics appear**, ensure:
- Label `.txt` files exist and are properly formatted.
- `val/labels/` and `test/labels/` are not empty.

---

## Interpretation
- Check `results.png` for signs of overfitting or undertraining.
- Use `confusion_matrix.png` to identify class imbalance or misclassification patterns.

