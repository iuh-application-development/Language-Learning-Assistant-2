from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.EmailField(
    widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'type': 'email',
        'placeholder': 'Email Address'
        })
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'type': 'password',
        'placeholder': 'Password'
        })
    )
    
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        
        if not email or not password:
            raise forms.ValidationError('email or password is required')
        
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('email or password is not correct')
        
        self.user = user
        return self.cleaned_data
    
    
    def get_user(self):
        return getattr(self, 'user', None)