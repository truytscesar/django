from django.shortcuts import render
from django.http import request
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import MyUserCreationForm
from django.http import JsonResponse
from .models import AcaoBtn
from datetime import datetime



def inicial(request):
    return render(request, 'app_deteriora/inicial.html')


def signin(request):
    return render(request, 'app_deteriora/signin.html')

'''
def signup(request):
    return render(request, 'app_deteriora/signup.html')
'''

def semi(request):
    return render(request, 'app_deteriora/semi.html')

def coro(request):
    return render(request, 'app_deteriora/coro.html')

def neuro(request):
    return render(request, 'app_deteriora/neuro.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import MyUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('signin')
    else:
        form = MyUserCreationForm()
    return render(request, 'app_deteriora/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        username = authenticate(request, username=username, password=password)
        if username is not None:
            login(request, username)
            messages.success(request, 'You have successfully signed in!')
            return redirect('semi')
    form = MyUserCreationForm()
    return render(request, 'app_deteriora/signin.html', {'form': form})


from .models import Teste
def get_date(request):
    if request.method == 'POST':
        date = 'x'
        date.save()
    return (request, 'app_deteriora/acao_registrada.html')