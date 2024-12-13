import os
import shutil
import random

# 학습-검증 데이터 분리 비율
TRAIN_RATIO = 0.8

def split_data(image_dir, label_dir, train_dir, val_dir):
    # 디렉토리 생성
    os.makedirs(os.path.join(train_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(train_dir, "labels"), exist_ok=True)
    os.makedirs(os.path.join(val_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(val_dir, "labels"), exist_ok=True)

    # 이미지와 라벨 파일 가져오기
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
    random.shuffle(image_files)

    train_size = int(len(image_files) * TRAIN_RATIO)
    train_images = image_files[:train_size]
    val_images = image_files[train_size:]

    # 파일 이동
    for image_file in train_images:
        shutil.copy(os.path.join(image_dir, image_file), os.path.join(train_dir, "images", image_file))
        label_file = image_file.replace('.jpg', '.txt')
        shutil.copy(os.path.join(label_dir, label_file), os.path.join(train_dir, "labels", label_file))

    for image_file in val_images:
        shutil.copy(os.path.join(image_dir, image_file), os.path.join(val_dir, "images", image_file))
        label_file = image_file.replace('.jpg', '.txt')
        shutil.copy(os.path.join(label_dir, label_file), os.path.join(val_dir, "labels", label_file))

# 경로 설정
image_dir = "C:/Users/jykim/Document/abs/data/raw/images"  # 이미지 경로
label_dir = "C:/Users/jykim/Document/abs/data/processed/labels"  # 라벨 경로
train_dir = "C:/Users/jykim/Document/abs/data/processed/train"  # 학습 데이터 경로
val_dir = "C:/Users/jykim/Document/abs/data/processed/val"  # 검증 데이터 경로

# 실행
split_data(image_dir, label_dir, train_dir, val_dir)
print("데이터가 train/val로 나뉘었습니다.")
