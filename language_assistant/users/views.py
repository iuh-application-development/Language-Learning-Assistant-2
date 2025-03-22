from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard:home')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()
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



