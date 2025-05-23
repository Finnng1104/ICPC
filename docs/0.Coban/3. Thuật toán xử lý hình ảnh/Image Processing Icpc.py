# ICPC - Xử lý hình ảnh offline (OpenCV, AI, mô hình nhẹ)
# Bao gồm: đọc ảnh, xử lý ảnh, nhận dạng bằng mô hình nhẹ

import cv2
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models

# ==== 1. Đọc ảnh với OpenCV và Pillow ====
img_cv = cv2.imread('sample.jpg')         # đọc bằng OpenCV
img_pil = Image.open('sample.jpg')        # đọc bằng Pillow

# ==== 2. Tiền xử lý ảnh cơ bản ====
# Resize, chuyển grayscale, threshold
resized = cv2.resize(img_cv, (224, 224))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# ==== 3. Tách vật thể (Contours) ====
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(resized, contours, -1, (0,255,0), 2)

# ==== 4. Nhận diện ảnh bằng mô hình CNN nhẹ (torchvision) ====
# Tải mô hình ResNet18 (có thể thay bằng MobileNetV2)
model = models.resnet18(pretrained=True)
model.eval()

# Chuyển ảnh từ Pillow thành tensor phù hợp
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
input_tensor = transform(img_pil).unsqueeze(0)

# Dự đoán
with torch.no_grad():
    output = model(input_tensor)
    predicted = torch.argmax(output, 1).item()

print("ID lớp dự đoán:", predicted)

# ==== 5. Nếu dùng ONNX model offline ====
# import onnxruntime
# ort_session = onnxruntime.InferenceSession("model.onnx")
# outputs = ort_session.run(None, {"input": input_numpy})

print("\n✅ Đã tích hợp xử lý ảnh offline, OpenCV, CNN model nhận diện đơn giản.")
