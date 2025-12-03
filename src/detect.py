# src/detect.py

from ultralytics import YOLO
import cv2

# Load the trained YOLOv8 model
model = YOLO("best.pt")

# Source (change to image path or video path)
source = ""   # image/video path

# Run detection
results = model.predict(source=source, show=True, conf=0.5, save=True ,show_boxes=False)

print("✅ Detection completed! Results are saved in 'runs/detect' folder.")