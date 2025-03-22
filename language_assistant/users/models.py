from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class MyUserManager(UserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # if not extra_fields.get('is_staff'):
        #     raise ValueError('set is_staff')
        # if not extra_fields.get('is_superuser'):
        #     raise ValueError('set is_superuser')
        
        return self.create_user(email, password, **extra_fields)
    
    
class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()