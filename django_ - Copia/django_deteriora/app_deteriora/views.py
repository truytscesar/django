from django.shortcuts import render
from django.http import request
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.base import TemplateView

def inicial(request):
    return render(request, 'app_deteriora/inicial.html')

'''
def login(request):
    return render(request, 'app_deteriora/login.html')

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
from .forms import EmailPasswordSignupForm


def signup(request):
    if request.method == 'POST':
        form = EmailPasswordSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = EmailPasswordSignupForm()
    return render(request, 'app_deteriora/signup.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import EmailPasswordForm

'''

def signup(request):
    form = EmailPasswordSignupForm()
    return render(request, 'signup.html', {'form': form})
'''

def login(request):
    if request.method == 'POST':
        form = EmailPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # process the form data as needed
            return redirect('semi')
    else:
        form = EmailPasswordForm()
    return render(request, 'app_deteriora/login.html', {'form': form})
