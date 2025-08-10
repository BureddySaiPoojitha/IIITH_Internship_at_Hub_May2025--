import os
from PIL import Image

def create_yolo_txt(image_path, bbox_list, class_id=0):
    """
    bbox_list: list of tuples (x_min, y_min, x_max, y_max) in pixels
    """
    img = Image.open(image_path)
    w, h = img.size
    lines = []
    for (xmin, ymin, xmax, ymax) in bbox_list:
        x_center = ((xmin + xmax) / 2) / w
        y_center = ((ymin + ymax) / 2) / h
        width = (xmax - xmin) / w
        height = (ymax - ymin) / h
        lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
    
    txt_path = os.path.splitext(image_path)[0] + ".txt"
    with open(txt_path, 'w') as f:
        f.write("\n".join(lines))

# Example usage:
# create_yolo_txt('images/train/card1.jpg', [(50, 30, 200, 180)], class_id=0)
