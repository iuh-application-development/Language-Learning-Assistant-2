from django.urls import path
from . import views

app_name = 'dictionary'

urlpatterns = [
    path('dictionary/', views.dictionary, name='dictionary'),
]
