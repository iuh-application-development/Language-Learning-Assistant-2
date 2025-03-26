from .views import flashcard_list, flashcard_detail, flashcard_new, flashcard_edit, flashcard_delete, category_new, category_delete
from django.urls import path

app_name = 'flashcard'

urlpatterns = [
    path('flashcard/', flashcard_list, name='flashcard_list'),
    path('flashcard/<int:pk>/', flashcard_detail, name='flashcard_detail'),
    path('flashcard/new/', flashcard_new, name='flashcard_new'),
    path('flashcard/<int:pk>/edit/', flashcard_edit, name='flashcard_edit'),
    path('flashcard/<int:pk>/delete/', flashcard_delete, name='flashcard_delete'),
    path('category/new/', category_new, name='category_new'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
]