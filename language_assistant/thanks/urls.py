from django.urls import path
from .views import thanks, serve_video, so_close_so_far, memorable, recall, word_apart

urlpatterns = [
    path('thanks/', thanks, name='thanks'),
    path('thanks/so_close_so_far/', so_close_so_far, name='so_close_so_far'),
    path('thanks/memorable/', memorable, name='memorable'),
    path('thanks/recall/', recall, name='recall'),
    path('thanks/world_apart/', word_apart, name='world_apart')
]