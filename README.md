# Nhóm 21

## Thành viên:
- **Trần Thái Nguyên** - *22697051*
- **Nguyễn Ngọc Minh** - *22685841*
- **Phan Công Chiến** - *22685651*
- **Trần Khắc Liêm** - *22685251*

<!-- admin@gmail.com -->
<!-- IUH@1234 -->

---
# Hướng Dẫn Sử Dụng Django


## **1. Chạy Server Django**
```bash
python manage.py runserver
```
- Khởi động server phát triển của Django.  
- Mặc định chạy tại `http://127.0.0.1:8000/`.  
- Dừng server bằng **`Ctrl + C`**.  

---

## **2. Tạo Và Áp Dụng Migrations**
### **Tạo File Migration**
```bash
python manage.py makemigrations
```
- Tạo file migration sau khi chỉnh sửa models.  

### **Áp Dụng Migration**
```bash
python manage.py migrate
```
- Cập nhật database theo các file migration đã tạo.  

---

## **3. Tạo Tài Khoản Admin**
```bash
python manage.py createsuperuser
```
- Tạo tài khoản quản trị viên để đăng nhập vào `/admin`.  
- Nhập thông tin:  
  - **Username**  
  - **Email** *(tuỳ chọn)*  
  - **Password**  

---

## **4. Mở Django Shell**
```bash
python manage.py shell
```
- Mở Python shell để thử nghiệm lệnh hoặc truy vấn dữ liệu.  

---

## **5. Lưu Ý Quan Trọng**
- Kích hoạt môi trường ảo trước khi chạy lệnh (nếu có):  
  ```bash
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
  ```
- Kiểm tra phiên bản Django:  
  ```bash
  python -m django --version
  ```

# Hướng dẫn clone responsitory
Chắc chắn rồi! Dưới đây là hướng dẫn chi tiết cách **clone một repository** từ GitHub hoặc GitLab về máy tính của bạn.

---

## 🧩 1. Cài đặt Git (nếu chưa có)

### 🖥 Trên Windows:
Tải Git tại: [https://git-scm.com/download/win](https://git-scm.com/download/win)  
Chạy file `.exe` và cài đặt như phần mềm bình thường.

### 💻 Trên Ubuntu/Debian:
```bash
sudo apt update
sudo apt install git
```

---

## 📥 2. Clone repository

### 🧪 Cú pháp:

Clone vềvề repo trên GitHub:
```bash
git clone https://github.com/iuh-application-development/Language-Learning-Assistant-2.git
```

Hoặc nếu bạn dùng SSH (bắt buộc phải có SSH key):
```bash
git clone git@github.com:iuh-application-development/Language-Learning-Assistant-2.git
```

---

# Hướng dẫn chạy ứng dụng

Chạy file `install.bat` để khởi động ứng dụng

