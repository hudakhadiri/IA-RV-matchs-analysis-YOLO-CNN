from ultralytics import YOLO

model = YOLO('yolov8x')
model.track('input_videos/input_video.mp4',save=True)
