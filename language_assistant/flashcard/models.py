from django.db import models
from users.models import MyUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)

    class Meta:
        unique_together = ['name', 'user']  # Tên category chỉ unique trong phạm vi của mỗi user

    def __str__(self):
        return f"{self.name} ({self.user.email if self.user else 'No User'})"

class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='flashcards', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-created_at']  # Sắp xếp theo thời gian tạo mới nhất