import cv2
import os

frame_folder = "detected_frames"
output_file = "output_detected_video.mp4"

frames = sorted(os.listdir(frame_folder))
first_frame = cv2.imread(os.path.join(frame_folder, frames[0]))
h, w, _ = first_frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, 30.0, (w, h))

for f in frames:
    frame = cv2.imread(os.path.join(frame_folder, f))
    out.write(frame)

out.release()
print(f"Video saved as {output_file}")
