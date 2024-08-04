
from ultralytics import YOLO
if  __name__ == "__main__":
    weight = "C:/Users/box15/Downloads/ultralytics/runs/detect/train57/weights/best.pt"
    source = "C:/Users/box15/Downloads/ultralytics/dataset/images/val2017"
    model  = YOLO(weight)
    results = model(source=source,save=True,show=True)
