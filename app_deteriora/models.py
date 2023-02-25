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
    
# Escolha de leitos para o botão Ação    
choices_leitos = [
            ('leito1', 'leito1'),
            ('leito2', 'leito2'),
            ('leito3', 'leito3')]

CHOICES_leitos = choices_leitos

class DataAtual(models.Model):
    leito = models.CharField(max_length=200, choices=CHOICES_leitos) 
    created_at = models.DateTimeField(auto_now_add=True)

# Escolha de leitos para o Gráfico Neuro 
choices_leitos_grafico = [
            ('A877', 'A877'),
            ('leito2', 'leito2'),
            ('leito3', 'leito3')]

CHOICES_leitos = choices_leitos_grafico

class LeitosGraficos(models.Model):
    leitos_graficos_neuro = models.CharField(max_length=200, choices=CHOICES_leitos) 
   

