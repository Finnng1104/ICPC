# ICPC - Xử lý hình ảnh offline (OpenCV, AI, mô hình nhẹ)
# Bao gồm: đọc ảnh, xử lý ảnh, nhận dạng bằng mô hình nhẹ
# Ứng dụng: Nhận dạng đối tượng, xử lý ảnh, AI nhẹ cho thiết bị di động

import cv2
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models

# ==== 0. Giới thiệu và ứng dụng thực tế ====
"""
Các thuật toán xử lý ảnh có nhiều ứng dụng trong thực tế:

1. Xử lý ảnh cơ bản:
   - Chỉnh sửa ảnh (resize, crop, filter)
   - Tăng cường chất lượng ảnh
   - Nén ảnh
   - Chuyển đổi định dạng

2. Nhận dạng đối tượng:
   - Phát hiện vật thể
   - Đếm đối tượng
   - Phân loại ảnh
   - OCR (nhận dạng chữ)

3. AI nhẹ:
   - Chạy trên thiết bị di động
   - Xử lý offline
   - Tối ưu hóa tốc độ
   - Tiết kiệm bộ nhớ

Ví dụ thực tế:
1. Camera giám sát thông minh
2. Ứng dụng chỉnh sửa ảnh
3. Nhận dạng khuôn mặt
4. Quét mã QR/Barcode
"""

# ==== 1. Đọc ảnh với OpenCV và Pillow ====
"""
Mục đích: Đọc ảnh từ file vào bộ nhớ để xử lý

Cách hoạt động (cho người mới):
1. OpenCV (cv2):
   - Đọc ảnh dưới dạng mảng numpy
   - Màu sắc theo thứ tự BGR (Blue, Green, Red)
   - Phù hợp với xử lý ảnh và computer vision

2. Pillow (PIL):
   - Đọc ảnh dưới dạng đối tượng Image
   - Màu sắc theo thứ tự RGB (Red, Green, Blue)
   - Phù hợp với hiển thị và lưu trữ

Ví dụ thực tế:
- Đọc ảnh từ camera
- Đọc ảnh từ thư mục
- Đọc ảnh từ URL
"""

def read_image(image_path):
    """Đọc ảnh với xử lý lỗi"""
    try:
        # Đọc bằng OpenCV (phù hợp xử lý ảnh)
        img_cv = cv2.imread(image_path)
        if img_cv is None:
            raise Exception("Không đọc được ảnh bằng OpenCV")
            
        # Đọc bằng Pillow (phù hợp hiển thị)
        img_pil = Image.open(image_path)
        
        return img_cv, img_pil
    except Exception as e:
        print(f"Lỗi đọc ảnh: {e}")
        return None, None

# ==== 2. Tiền xử lý ảnh cơ bản ====
"""
Mục đích: Chuẩn bị ảnh cho các bước xử lý tiếp theo

Các bước xử lý cơ bản:
1. Resize: Thay đổi kích thước ảnh
   - Chuẩn hóa kích thước
   - Giảm độ phức tạp xử lý
   - Phù hợp với model AI

2. Grayscale: Chuyển ảnh sang đen trắng
   - Giảm kênh màu
   - Tập trung vào cấu trúc
   - Phù hợp với xử lý biên

3. Threshold: Phân đoạn ảnh
   - Tách đối tượng khỏi nền
   - Tạo ảnh nhị phân
   - Phù hợp với tìm contour

Ví dụ thực tế:
- Chuẩn hóa ảnh cho AI
- Tách đối tượng khỏi nền
- Tăng cường độ tương phản
"""

def preprocess_image(image, target_size=(224, 224)):
    """Tiền xử lý ảnh với các bước cơ bản"""
    # 1. Resize về kích thước chuẩn
    resized = cv2.resize(image, target_size)
    
    # 2. Chuyển sang grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    
    # 3. Áp dụng threshold
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # 4. Tăng cường độ tương phản (tùy chọn)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    return {
        'resized': resized,
        'gray': gray,
        'thresh': thresh,
        'enhanced': enhanced
    }

# ==== 3. Tách vật thể (Contours) ====
"""
Mục đích: Tìm và phân tích các đối tượng trong ảnh

Cách hoạt động (cho người mới):
1. Tìm contour:
   - Phát hiện biên của đối tượng
   - Tạo đường viền liên tục
   - Phân biệt các đối tượng

2. Phân tích contour:
   - Tính diện tích
   - Tính chu vi
   - Tìm hình dạng

3. Vẽ contour:
   - Hiển thị kết quả
   - Đánh dấu đối tượng
   - Phân loại theo màu

Ví dụ thực tế:
- Đếm số lượng đối tượng
- Phát hiện khuyết tật
- Phân tích hình dạng
"""

def find_objects(image, min_area=100):
    """Tìm và phân tích các đối tượng trong ảnh"""
    # 1. Tiền xử lý
    processed = preprocess_image(image)
    
    # 2. Tìm contour
    contours, hierarchy = cv2.findContours(
        processed['thresh'],
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )
    
    # 3. Phân tích từng contour
    objects = []
    for contour in contours:
        # Tính diện tích
        area = cv2.contourArea(contour)
        if area < min_area:
            continue
            
        # Tính chu vi
        perimeter = cv2.arcLength(contour, True)
        
        # Tìm hình dạng gần đúng
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
        num_vertices = len(approx)
        
        # Phân loại hình dạng
        shape = "unknown"
        if num_vertices == 3:
            shape = "triangle"
        elif num_vertices == 4:
            shape = "rectangle"
        elif num_vertices > 4:
            shape = "circle"
            
        objects.append({
            'contour': contour,
            'area': area,
            'perimeter': perimeter,
            'shape': shape
        })
    
    # 4. Vẽ kết quả
    result = processed['resized'].copy()
    for obj in objects:
        # Vẽ contour
        cv2.drawContours(result, [obj['contour']], -1, (0,255,0), 2)
        
        # Vẽ thông tin
        M = cv2.moments(obj['contour'])
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.putText(result, obj['shape'], (cx, cy),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    
    return result, objects

# ==== 4. Nhận diện ảnh bằng mô hình CNN nhẹ ====
"""
Mục đích: Phân loại ảnh sử dụng deep learning

Cách hoạt động (cho người mới):
1. Mô hình CNN:
   - Học đặc trưng từ ảnh
   - Phân loại đối tượng
   - Chạy trên GPU/CPU

2. Tiền xử lý:
   - Resize về kích thước chuẩn
   - Chuẩn hóa giá trị pixel
   - Chuyển đổi định dạng

3. Dự đoán:
   - Tính toán forward pass
   - Lấy kết quả có xác suất cao nhất
   - Ánh xạ về nhãn thực tế

Ví dụ thực tế:
- Nhận dạng đối tượng
- Phân loại ảnh
- Phát hiện bất thường
"""

def load_model(model_name='resnet18'):
    """Tải và chuẩn bị mô hình"""
    # 1. Chọn mô hình
    if model_name == 'resnet18':
        model = models.resnet18(pretrained=True)
    elif model_name == 'mobilenet':
        model = models.mobilenet_v2(pretrained=True)
    else:
        raise ValueError(f"Không hỗ trợ mô hình {model_name}")
    
    # 2. Chuyển sang chế độ đánh giá
    model.eval()
    
    # 3. Chuẩn bị transform
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    
    return model, transform

def predict_image(model, transform, image, class_names):
    """Dự đoán ảnh và trả về kết quả"""
    # 1. Tiền xử lý ảnh
    if isinstance(image, np.ndarray):
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    # 2. Chuyển đổi tensor
    input_tensor = transform(image).unsqueeze(0)
    
    # 3. Dự đoán
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        
        # Lấy top 3 kết quả
        top3_prob, top3_catid = torch.topk(probabilities, 3)
        
        results = []
        for i in range(3):
            results.append({
                'class': class_names[top3_catid[i].item()],
                'probability': top3_prob[i].item()
            })
    
    return results

# ==== 5. Tối ưu hóa cho thiết bị di động ====
"""
Mục đích: Chạy mô hình AI trên thiết bị di động

Các phương pháp tối ưu:
1. Quantization:
   - Giảm độ chính xác số
   - Giảm kích thước model
   - Tăng tốc độ xử lý

2. ONNX Runtime:
   - Chạy model offline
   - Tối ưu hóa cross-platform
   - Hỗ trợ nhiều hardware

3. Model nhẹ:
   - MobileNet
   - EfficientNet
   - SqueezeNet

Ví dụ thực tế:
- Ứng dụng di động
- Xử lý offline
- Edge computing
"""

def optimize_for_mobile(model, save_path):
    """Tối ưu hóa model cho thiết bị di động"""
    # 1. Quantization
    quantized_model = torch.quantization.quantize_dynamic(
        model, {torch.nn.Linear}, dtype=torch.qint8
    )
    
    # 2. Export sang ONNX
    dummy_input = torch.randn(1, 3, 224, 224)
    torch.onnx.export(
        quantized_model,
        dummy_input,
        save_path,
        export_params=True,
        opset_version=10,
        do_constant_folding=True,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={
            'input': {0: 'batch_size'},
            'output': {0: 'batch_size'}
        }
    )
    
    return save_path

# ==== Demo ====
if __name__ == "__main__":
    print("\n=== Demo xử lý ảnh với các thuật toán đã học ===")
    
    # 1. Đọc ảnh
    image_path = "sample.jpg"
    img_cv, img_pil = read_image(image_path)
    if img_cv is None:
        print("Không đọc được ảnh, sử dụng ảnh mẫu")
        img_cv = np.zeros((224, 224, 3), dtype=np.uint8)
        img_cv[50:150, 50:150] = [0, 255, 0]  # Vẽ hình vuông xanh
    
    # 2. Tiền xử lý
    processed = preprocess_image(img_cv)
    print("Đã xử lý ảnh với các bước cơ bản")
    
    # 3. Tìm đối tượng
    result, objects = find_objects(img_cv)
    print(f"Tìm thấy {len(objects)} đối tượng")
    for obj in objects:
        print(f"- {obj['shape']}: diện tích={obj['area']:.0f}")
    
    # 4. Nhận diện ảnh
    model, transform = load_model('resnet18')
    class_names = ['cat', 'dog', 'bird']  # Ví dụ
    predictions = predict_image(model, transform, img_pil, class_names)
    print("\nTop 3 dự đoán:")
    for pred in predictions:
        print(f"- {pred['class']}: {pred['probability']:.2%}")
    
    # 5. Tối ưu hóa
    if torch.cuda.is_available():
        print("\nTối ưu hóa model cho thiết bị di động...")
        model_path = optimize_for_mobile(model, "model_mobile.onnx")
        print(f"Đã lưu model tối ưu tại: {model_path}")
    
    print("\n✅ Đã demo xử lý ảnh với các thuật toán cơ bản và AI.")
