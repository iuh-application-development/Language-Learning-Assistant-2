from django.urls import path
from .views import login_view, register, logout_view, profile, profile_edit
from django.conf import settings
from django.conf.urls.static import static  
app_name ='users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]

# Thêm cấu hình media trong chế độ debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)