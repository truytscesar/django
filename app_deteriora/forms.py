from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


from .models import DataAtual,LeitosGraficos
from django.forms import ModelForm

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class DataAtualForm(ModelForm):
    class Meta:
        model = DataAtual
        fields = '__all__'

class LeitosGraficosForm(ModelForm):
    class Meta:
        model = LeitosGraficos
        fields = '__all__'


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Senha incorreta",
    }
