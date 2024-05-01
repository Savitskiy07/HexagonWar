from django.db import models

class Registration(models.Model):
    username = models.CharField('Имя пользователя', max_length=15)
    password = models.CharField('Пароль', max_length=15)
    
    def __str__(self) -> str:
        return self.username
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    
    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'

    
    