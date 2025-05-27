from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm, ForgotPasswordForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.firebase_helpers import firebase_config

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            user_instance = form.get_user_instance()
            
            login(request, user_instance)
            request.session['uid'] = str(user['idToken'])
            return redirect('dashboard:home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = UserLoginForm()
        storage = messages.get_messages(request)
        storage.used = True
    context = {
        'form': form,
        'errors': form.errors
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # # Đăng nhập tự động sau khi đăng ký (tùy chọn)
            # firebase = firebase_config()
            # auth = firebase.auth()
            # user_record = auth.sign_in_with_email_and_password(
            #     form.cleaned_data['email'],
            #     form.cleaned_data['password1']
            # )
            # request.session['uid'] = user_record['localId']
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('user:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = UserRegisterForm() 
        storage = messages.get_messages(request)
        storage.used = True
    context = {
        'form': form,
        'errors': form.errors
    }
    return render(request, 'users/signup.html', context)

def logout_view(request):
    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'yes':
            logout(request)
            messages.success(request, 'Bạn đã đăng xuất thành công!')
            return redirect('users:login')
        elif confirm == 'no':
            return redirect('dashboard:home')  # Hoặc trang chính mà bạn muốn chuyển đến
    return render(request, 'users/logout.html')


def profile(request):
    return render(request, 'users/profile.html')


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            firebase = firebase_config()
            auth = firebase.auth()

            try:
                # Gửi email đặt lại mật khẩu
                auth.send_password_reset_email(email)
                print(f"Password reset email sent to: {email}")
                messages.success(request, "A password reset link has been sent to your email.")
                return redirect('user:forgot_password')  # Hoặc chuyển hướng đến trang khác
            except Exception as e:
                error_msg = str(e)
                print(f"Firebase reset password error: {error_msg}")
                if "EMAIL_NOT_FOUND" in error_msg:
                    messages.error(request, "No account found with this email address.")
                elif "INVALID_EMAIL" in error_msg:
                    messages.error(request, "Invalid email address.")
                else:
                    messages.error(request, f"Failed to send reset email: {error_msg}")
                return render(request, 'users/forgot_password.html', {'form': form})
        else:
            print(form.errors)
    else:
        form = ForgotPasswordForm()

    return render(request, 'users/forgot_password.html', {'form': form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('users:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile_edit.html', {'form': form})
