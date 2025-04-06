from django.urls import path
from .views import quiz

app_name = 'quiz'

urlpatterns = [
    path('quiz/', quiz, name='quiz'),
]