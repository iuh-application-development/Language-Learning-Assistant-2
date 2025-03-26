from django.db import models
from users.models import MyUser
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.question