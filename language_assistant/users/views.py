from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print('11111')
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def register(request):
    return render(request, 'users/signup.html')