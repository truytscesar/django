from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import (
    inicial, signin, signup, semi, coro, neuro
)

urlpatterns = [
    path('', inicial, name = 'inicial'),
    path('signin', signin, name = 'signin'),
    path('signup', signup, name = 'signup'),
    path('semi', semi, name = 'semi'),
    path('coro', coro, name = 'coro'),
    path('neuro', neuro, name = 'neuro'),
]


