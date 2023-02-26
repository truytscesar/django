LOGIN_URL = 'signin'

# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .forms import CustomAuthenticationForm

from .views import (
    signup, semi, coro, neuro, my_view, neuro_grafico
)

urlpatterns = [
    path('', auth_views.LogoutView.as_view(template_name='app_deteriora/inicial.html')),
    path('signin/', auth_views.LoginView.as_view(template_name='app_deteriora/signin.html', authentication_form=CustomAuthenticationForm), name='signin'),
    path('accounts/profile/inicial', auth_views.LogoutView.as_view(template_name='app_deteriora/inicial.html')),
    path('signup', signup, name = 'signup'),
    path('accounts/profile/', semi, name = 'semi'),
    path('accounts/profile/semi', semi, name = 'semi'),
    path('accounts/profile/coro', coro, name = 'coro'),
    path('accounts/profile/neuro', neuro, name = 'neuro'),
    path('accounts/profile/my_view', my_view, name = 'my_view'),
    path('accounts/profile/neuro_grafico', neuro_grafico, name = 'neuro_grafico'),
]




