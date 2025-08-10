import cv2
import os
import glob

# ===== User chooses train or valid =====
set_type = input("Type 'train' or 'valid': ").strip().lower()
if set_type not in ["train", "valid"]:
    print("Invalid choice. Please run again and type 'train' or 'valid'.")
    exit()

# Paths
images_folder = os.path.join("images", set_type)
labels_folder = os.path.join("labels", set_type)
os.makedirs(labels_folder, exist_ok=True)

# Load all image paths (jpg, jpeg, png)
images = sorted(
    glob.glob(os.path.join(images_folder, "*.jpg")) +
    glob.glob(os.path.join(images_folder, "*.jpeg")) +
    glob.glob(os.path.join(images_folder, "*.png"))
)

if not images:
    print(f"No images found in {images_folder}")
    exit()

print(f"Found {len(images)} images in {images_folder}")

# Global variables for mouse events
drawing = False
ix, iy = -1, -1
boxes = []
current_class = 0  # 0 = safe, 1 = alert

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, boxes, current_class
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x_min, y_min = min(ix, x), min(iy, y)
        x_max, y_max = max(ix, x), max(iy, y)
        boxes.append((current_class, x_min, y_min, x_max, y_max))

# Main labeling loop
for img_path in images:
    boxes = []
    img_name = os.path.basename(img_path)
    label_path = os.path.join(labels_folder, img_name.rsplit(".", 1)[0] + ".txt")

    img = cv2.imread(img_path)
    if img is None:
        print(f"Error loading image {img_name}")
        continue

    cv2.namedWindow("YOLO Label Tool")
    cv2.setMouseCallback("YOLO Label Tool", draw_rectangle)

    while True:
        display_img = img.copy()

        # Draw current boxes
        for cls, x1, y1, x2, y2 in boxes:
            color = (0, 255, 0) if cls == 0 else (0, 0, 255)
            cv2.rectangle(display_img, (x1, y1), (x2, y2), color, 2)
            cv2.putText(display_img, str(cls), (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        cv2.imshow("YOLO Label Tool", display_img)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('0'):
            current_class = 0
            print("Class set to SAFE (0)")
        elif key == ord('1'):
            current_class = 1
            print("Class set to ALERT (1)")
        elif key == ord('n'):  # Next image
            break
        elif key == ord('s'):  # Save
            h, w = img.shape[:2]
            with open(label_path, "w") as f:
                for cls, x1, y1, x2, y2 in boxes:
                    x_center = ((x1 + x2) / 2) / w
                    y_center = ((y1 + y2) / 2) / h
                    bw = (x2 - x1) / w
                    bh = (y2 - y1) / h
                    f.write(f"{cls} {x_center} {y_center} {bw} {bh}\n")
            print(f"Saved labels for {img_name}")
        elif key == ord('q'):  # Quit
            cv2.destroyAllWindows()
            exit()

cv2.destroyAllWindows()
