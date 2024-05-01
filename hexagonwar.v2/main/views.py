from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'main/layout.html',)


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'login.html', {'error':'Имя пользователя уже существует'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('index')
        else:
            return render(request, 'login.html', {'error':'Пароли не совпадают'})
    else:
        return render(request, 'login.html')



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)    
                messages.success(request, f'Вы успешно вошли в систему, {username}!')
                return redirect('home')
            
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = AuthenticationForm()

    return render(request, 'main/login.html', {'form': form})


