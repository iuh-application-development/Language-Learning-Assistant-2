from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django.forms.widgets import ClearableFileInput

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.EmailField(
    widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'type': 'email',
        'placeholder': 'Email Address'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'type': 'password',
        'placeholder': 'Password'
    }))
    
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        if not email or not password:
            raise forms.ValidationError('Email or password is required')
        
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Email or password is not correct')
        
        self.user = user
        return self.cleaned_data
    
    
    def get_user(self):
        return getattr(self, 'user', None)
    
    

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'type': 'email',
        'placeholder': 'Email Address'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'id': 'password',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'id': 'password',
        'placeholder': 'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'bio', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'avatar': ClearableFileInput(attrs={'class': 'form-control'}),
        }