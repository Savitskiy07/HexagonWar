from .models import Registration
from django.forms import ModelForm, TextInput


class RegisterForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя игрока'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }