from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard:home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = UserLoginForm()
        # Xóa tất cả thông báo cũ khi load trang đăng nhập
        storage = messages.get_messages(request)
        storage.used = True
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Thay vì redirect với message, ta sẽ render trang signup với message thành công
            messages.success(request, 'Registration successful! You can now log in.')
            # Render lại trang signup với form mới và message thành công
            # return render(request, 'users/signup.html', {'form': UserRegisterForm()})
            return redirect('users:login')  # Chuyển hướng đến trang đăng nhập sau khi đăng ký thành công
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = UserRegisterForm()
        # Xóa tất cả thông báo cũ khi load trang đăng ký
        storage = messages.get_messages(request)
        storage.used = True
    return render(request, 'users/signup.html', {'form': form})

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
