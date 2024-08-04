from ultralytics import YOLO
if __name__ == '__main__':
    model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
    results = model.train(data='face.yaml', epochs=200,imgsz=640,batch=50,save =True,device=[0])

