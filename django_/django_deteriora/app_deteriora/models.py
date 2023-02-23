from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

class User(AbstractUser):
    # Add related_name argument to avoid clashes with the built-in User model
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_set', blank=True
    )

class MyUserCreationForm(models.Model):
    dados_de_login = ('username', 'email', 'password1', 'password2')
    
class AcaoBtn(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    
class Teste(models.Model):
    date = models.CharField(max_length=20, date='x')