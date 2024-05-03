from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'main/layout.html',)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, '../templates/main/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Пользователь с таким именем не существует или введен неверный пароль')
    else:
        form = LoginForm()
    return render(request, '../templates/main/login.html', {'form': form})








