# **Task 2: Object Detection in Video using YOLOv8**

This project performs object detection on each frame of a YouTube video using **YOLOv8**, and reassembles the annotated frames into a final output video.

---

## Input

- **YouTube Short**: [Watch Here](https://youtube.com/shorts/E6St30L9Jv0?si=GM9cvFRTBn4cronm)
- Downloaded and saved as `input_video.mp4` using `yt-dlp`.

---

## 🛠️ Steps Performed

1. **Download Video**  
   ```bash
   yt-dlp -o input_video.mp4 "<video_url>"
   ```

2. **Extract Frames**  
   `extract_frames.py` saves individual frames to "frames/" folder.

3. **Object Detection (YOLOv8)**  
   `detect_objects.py` runs YOLOv8 on all frames using "yolov8n.pt".

4. **Reconstruct Video**  
   `make_video.py` merges annotated frames into "output_detected_video.mp4".

---

## Folder Structure

```
TASK-2/
│
  ── input_video.mp4
| ── extract_frames.py
  ── detect_objects.py
| ── make_video.py
  ── README.md
│
  ── frames/
│
    └── frame_0000.jpg ...
│
  ── detected_frames/
     └── frame_0000.jpg ...
```

---

## Tech Stack

- Python + OpenCV
- Ultralytics YOLOv8
- yt-dlp (video download)



## Output

- Final annotated video: "output_detected_video.mp4"