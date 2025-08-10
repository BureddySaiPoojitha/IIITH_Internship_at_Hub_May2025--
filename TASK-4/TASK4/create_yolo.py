import os
from PIL import Image

def create_yolo_txt(image_path, bbox_list, class_id=0):
    img = Image.open(image_path)
    w, h = img.size
    lines = []
    for (xmin, ymin, xmax, ymax) in bbox_list:
        x_center = ((xmin + xmax) / 2) / w
        y_center = ((ymin + ymax) / 2) / h
        width = (xmax - xmin) / w
        height = (ymax - ymin) / h
        lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")
    txt_path = os.path.splitext(image_path)[0].replace('images', 'labels') + ".txt"
    os.makedirs(os.path.dirname(txt_path), exist_ok=True)
    with open(txt_path, 'w') as f:
        f.write("\n".join(lines))
    print(f"Saved labels to {txt_path}")

def pair_images_labels(image_dir, label_dir):
    exts = {'.jpg', '.jpeg', '.png'}
    image_files = []
    for root, _, files in os.walk(image_dir):
        for f in files:
            if os.path.splitext(f)[1].lower() in exts:
                image_files.append(os.path.join(root, f))

    paired = []
    for img_path in image_files:
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        lbl_path = os.path.join(label_dir, os.path.relpath(os.path.dirname(img_path), image_dir), base_name + '.txt')
        if os.path.exists(lbl_path):
            paired.append((img_path, lbl_path))
        else:
            print(f"Warning: No label for {img_path}")
    return paired

if __name__ == "__main__":
    base_image_dir = r"C:\Users\Saipo\IIITH_Internship\TASK-4\TASK4\images"
    base_label_dir = r"C:\Users\Saipo\IIITH_Internship\TASK-4\TASK4\labels"

    train_pairs = pair_images_labels(os.path.join(base_image_dir, 'train'), os.path.join(base_label_dir, 'train'))
    valid_pairs = pair_images_labels(os.path.join(base_image_dir, 'valid'), os.path.join(base_label_dir, 'valid'))

    print(f"Train pairs found: {len(train_pairs)}")
    print(f"Valid pairs found: {len(valid_pairs)}")

    # Example: Visualize first train image with labels (reuse visualization code if needed)
