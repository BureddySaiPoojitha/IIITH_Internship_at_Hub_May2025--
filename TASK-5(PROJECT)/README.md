YASK -5 : Mobile-Use Detection in Drivers via YOLOv8: A Vision-Based Safety Solution

YOLO Label Tool

A simple Python tool to create bounding box annotations for YOLO object detection datasets.  
Supports both **train** and **valid** image folders, and works with `.jpg`, `.jpeg`, and `.png` images.

---

## Dataset Structure

The tool expects your dataset to be organized like this:

```
TASK-5/
│
|── images/
│   |─ train/
│   │   |─ img1.jpg
│   │   |─ img2.jpg
│   │   |─ ...
│   └── valid/
│       |─ imgA.jpg
│       |─ imgB.jpg
│       |─ ...
│
|─ labels/
    |─ train/
    |─ valid/
```

---

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Install requirements**
   ```bash
   pip install opencv-python
   ```

---

##  Usage

Run the script:

```bash
python yolo_label_tool.py
```

When prompted, type:
- `train` → to label training images
- `valid` → to label validation images

---

## Controls

| Key | Action |
|-----|--------|
| **Left Mouse Drag** | Draw a bounding box |
| **0** | Set current class to **SAFE** |
| **1** | Set current class to **ALERT** |
| **s** | Save labels for the current image |
| **n** | Move to the next image without saving |
| **q** | Quit the program |

---

##  Output Format

Labels are saved in YOLO format in:
```
labels/train/
labels/valid/
```

Each line in the `.txt` file contains:
```
<class_id> <x_center> <y_center> <width> <height>
```
All values are **normalized** between 0 and 1.

---

##  Example

Example label file (`img1.txt`):
```
0 0.5474 0.2596 0.1281 0.1923
1 0.3200 0.6000 0.2000 0.3000
```

---

##  Notes
- Make sure your `labels/` folder exists before running.
- If some images don't have labels, YOLO will skip them during training/validation.
- You can press `s` to save at any time before moving to the next image.

---

##  License
This project is licensed under the MIT License.
