#  ỨNG DỤNG TRỢ LÝ NGÔN NGỮ - LANGUAGE ASSISTANT

🌍 Về Language Assistant
Chào mừng bạn đến với Language Assistant – trợ lý ngôn ngữ cá nhân của bạn!

✨ Chúng tôi là ai?
Language Assistant là một nền tảng hỗ trợ học và sử dụng ngoại ngữ, được xây dựng với mong muốn giúp mọi người vượt qua rào cản ngôn ngữ trong học tập, công việc và cuộc sống hàng ngày.

Bắt đầu từ một ý tưởng đơn giản: "Nếu mỗi người đều có một trợ lý ngôn ngữ riêng, việc học ngoại ngữ sẽ dễ dàng và thú vị hơn rất nhiều!" – chúng tôi đã phát triển nên một ứng dụng thông minh, thân thiện và đầy cảm hứng cho người học ngôn ngữ ở mọi cấp độ.

⚙️ Language Assistant có thể giúp bạn:
✏️ Dịch thuật thông minh: Hỗ trợ dịch đa ngôn ngữ với văn phong tự nhiên, giữ đúng ngữ cảnh, có ví dụ minh họa rõ ràngràng.

<!-- 🧠 Sửa lỗi ngữ pháp và chính tả: Phân tích và gợi ý cách viết chuẩn xác hơn. -->

<!-- 🗣️ Luyện phát âm với AI: Nhận phản hồi tức thì và điều chỉnh phát âm theo giọng bản xứ. -->

💬 Hội thoại song ngữ: Giao tiếp mô phỏng hội thoại thực tế để luyện phản xạ ngôn ngữ.

📚 Gợi ý từ vựng theo ngữ cảnh: Mở rộng vốn từ theo chủ đề bạn đang học.

📈 Theo dõi tiến độ học tập: Cá nhân hóa lộ trình học theo trình độ và mục tiêu của bạn.

🎯 Tầm nhìn của chúng tôi
Chúng tôi tin rằng ngôn ngữ là chìa khóa kết nối thế giới.
Mục tiêu của chúng tôi là trở thành người bạn đồng hành đáng tin cậy cho hàng triệu người học ngôn ngữ trên toàn cầu, mang lại trải nghiệm học tập nhẹ nhàng, hiệu quả và đầy cảm hứng.

🤝 Tham gia cùng chúng tôi!
Dù bạn là người mới bắt đầu hay đã học nhiều năm, Language Assistant luôn sẵn sàng đồng hành cùng bạn.
👉 Hãy bắt đầu miễn phí hôm nay – và khám phá cách học ngoại ngữ thú vị hơn bạn từng nghĩ!

Nếu bạn có bất kỳ góp ý, câu hỏi hay mong muốn hợp tác, đừng ngần ngại liên hệ với chúng tôi qua email.


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

---

