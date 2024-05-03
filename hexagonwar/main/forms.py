from .models import Registration, Login
from django.forms import ModelForm, TextInput
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class LoginForm(AuthenticationForm):
    class Meta:
        model = Login
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя игрока'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error('username', 'Неверное имя пользователя или пароль')
            
        return cleaned_data


class RegisterForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя игрока'
            }),
            'password1': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
            'password2': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Подвердите пароль'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Пароли не совпадают")

        return cleaned_data
