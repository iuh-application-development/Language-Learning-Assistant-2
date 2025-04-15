# 🌏 LANGUAGE ASSISTANT - TRỢ LÝ NGÔN NGỮ

![alt text](image.png)

## 📝 Giới thiệu

Language Assistant là nền tảng hỗ trợ học và sử dụng ngoại ngữ thông minh, được thiết kế để giúp người dùng vượt qua rào cản ngôn ngữ trong học tập, công việc và cuộc sống hàng ngày.

Xuất phát từ triết lý: "Mỗi người đều xứng đáng có một trợ lý ngôn ngữ riêng", chúng tôi mang đến công cụ đa năng, thông minh và trực quan cho người học ở mọi trình độ.

## ✨ Tính năng chính

- **🔤 Dịch thuật thông minh**: Hỗ trợ dịch đa ngôn ngữ với văn phong tự nhiên, bám sát ngữ cảnh và cung cấp ví dụ minh họa
- **💬 Hội thoại tương tác**: Mô phỏng giao tiếp thực tế để rèn luyện phản xạ ngôn ngữ
- **📚 Gợi ý từ vựng theo chủ đề**: Mở rộng vốn từ theo lĩnh vực bạn quan tâm
- **📈 Theo dõi tiến độ học tập**: Cá nhân hóa lộ trình học phù hợp với mục tiêu của bạn

## 🛠️ Hướng dẫn cài đặt

### Yêu cầu hệ thống
- Python 3.8 trở lên
- Git
- Pip (Python Package Installer)

### 1. Cài đặt Git (nếu chưa có)

**Windows:**
- Tải Git tại: [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Chạy file `.exe` và làm theo hướng dẫn cài đặt

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install git
```

**macOS:**
```bash
brew install git
```

### 2. Clone repository

```bash
# Sử dụng HTTPS
git clone https://github.com/iuh-application-development/Language-Learning-Assistant-2.git

# Hoặc sử dụng SSH (cần cấu hình SSH key)
git clone git@github.com:iuh-application-development/Language-Learning-Assistant-2.git

# Di chuyển vào thư mục dự án
cd Language-Learning-Assistant-2
```

### 3. Cài đặt môi trường ảo và các phụ thuộc

**Windows:**
```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
venv\Scripts\activate

# Cài đặt các gói phụ thuộc
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo
source venv/bin/activate

# Cài đặt các gói phụ thuộc
pip install -r requirements.txt
```

### 4. Khởi động nhanh

Để cài đặt và chạy ứng dụng nhanh chóng, bạn có thể sử dụng script tự động:

**Windows:**
```bash
# Chạy file cài đặt tự động
install.bat
```

**Linux/macOS:**
```bash
# Cấp quyền thực thi cho script
chmod +x install.sh

# Chạy script cài đặt
./install.sh
```

# Hướng dẫn build docker image
 Nhập lệnh 
 ```
 docker build -t LanAssist .
 ```

## 🚀 Hướng dẫn sử dụng Django

### Chạy Server Django

Di chuyển vào thư mục language_assistant
```bash
cd language_assistant
```
Khởi động server

```bash
python manage.py runserver
```
- Server phát triển sẽ chạy tại địa chỉ mặc định: `http://127.0.0.1:8000/`
- Để dừng server, nhấn `Ctrl + C`

### Truy cập trang admin(cần tạo superuser trước)

- Trang admin sẽ chạy tại địa chỉ mặc định: `http://127.0.0.1:8000/admin`

### Quản lý Database (Migrations)

```bash
# Tạo file migration khi thay đổi models
python manage.py makemigrations

# Áp dụng migrations vào database
python manage.py migrate
```

### Tạo tài khoản quản trị viên

```bash
python manage.py createsuperuser
```
- Làm theo hướng dẫn để nhập thông tin tài khoản
- Sử dụng tài khoản này để đăng nhập tại đường dẫn `/admin`

### Công cụ phát triển và thử nghiệm

```bash
# Mở Django shell để thử nghiệm code và truy vấn dữ liệu
python manage.py shell

# Kiểm tra phiên bản Django đang sử dụng
python -m django --version
```

## 🔍 Cấu trúc dự án

Tham khảo structure.txt


## 🤝 Đóng góp

Chúng tôi luôn chào đón mọi đóng góp từ cộng đồng! Nếu bạn muốn tham gia phát triển dự án:

1. Fork repository này
2. Tạo nhánh tính năng (`git checkout -b feature/amazing-feature`)
3. Commit thay đổi của bạn (`git commit -m 'Add some amazing feature'`)
4. Push lên nhánh đã tạo (`git push origin feature/amazing-feature`)
5. Mở Pull Request

## 📞 Liên hệ và hỗ trợ

- **Email:**
- **Website:** 
- **GitHub Issues:** 
## 📜 Giấy phép


---


## 👥 Đội ngũ phát triển

| Họ và tên | Mã số sinh viên | Vai trò | Email | GitHub |
|-----------|----------------|---------|-------|--------|
| Nguyễn Ngọc Minh | 22685841 | Team Leader |  |  |
| Trần Thái Nguyên | 22697051 | Backend Developer | | [link](https://github.com/PlusNguyn) |
| Phan Công Chiến | 22685651 | Frontend Developer | |  |
| Trần Khắc Liêm | 22685251 | UI/UX Designer | |  |



---
© 2025 Language Assistant Team. All rights reserved