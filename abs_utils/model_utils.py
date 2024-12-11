import torch

def load_yolo_model():
    """
    YOLOv5 모델을 로드합니다.
    """
    # YOLOv5 기본 모델 로드 (COCO 데이터셋)
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # 'yolov5s'는 경량 YOLOv5 모델
    return model
