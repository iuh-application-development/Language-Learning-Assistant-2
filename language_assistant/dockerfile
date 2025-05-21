# ======= Stage 1: Build dependencies =======
FROM python:3.10 AS builder

# Đặt thư mục làm việc
WORKDIR /app

# Cài đặt pip và cập nhật
RUN pip install --upgrade pip

# Copy file yêu cầu và cài đặt các dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ======= Stage 2: Build Runtime Image =======
FROM python:3.10

# Đặt thư mục làm việc
WORKDIR /app

# Copy từ Stage 1 (chỉ giữ lại các gói đã cài đặt)
COPY --from=builder /install /usr/local

# Copy toàn bộ source code vào container
COPY . . 

# Chuyển vào thư mục chứa manage.py
WORKDIR /language_assistant

# Expose cổng 8000 cho Django
EXPOSE 8000

# Chạy migrations và khởi động server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]