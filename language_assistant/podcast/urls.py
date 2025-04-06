from django.urls import path, include
from .views import *

app_name = 'podcast'

urlpatterns = [
    path('podcast_list/', podcast_list, name='podcast_list'),
]