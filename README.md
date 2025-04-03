# Nhóm 21

## Thành viên:
- **Trần Thái Nguyên** - *22697051*
- **Nguyễn Ngọc Minh** - *22685841*
- **Phan Công Chiến** - *22002515*
- **Trần Khắc Liêm** - *22685251*

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

---

## **Kết Luận**
Trên đây là các lệnh quan trọng giúp bạn làm việc với Django. Nếu gặp lỗi, hãy kiểm tra lại môi trường hoặc liên hệ thành viên trong nhóm. 🚀
