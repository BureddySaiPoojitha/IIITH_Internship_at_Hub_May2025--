import cv2
import os

cap = cv2.VideoCapture("input_video.mp4")
os.makedirs("frames", exist_ok=True)

frame_num = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imwrite(f"frames/frame_{frame_num:04d}.jpg", frame)
    frame_num += 1

cap.release()
print(f"{frame_num} frames extracted.")
