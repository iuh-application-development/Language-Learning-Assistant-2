from django.urls import path
from .views import home, about, courses, team, testimonial, contact

app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('contact/', contact, name='contact'),
]