from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import (
    inicial, signin, signup, semi, coro, neuro, my_view, neuro_grafico
)

urlpatterns = [
    path('', inicial, name = 'inicial'),
    path('signin', signin, name = 'signin'),
    path('signup', signup, name = 'signup'),
    path('semi', semi, name = 'semi'),
    path('coro', coro, name = 'coro'),
    path('neuro', neuro, name = 'neuro'),
    path('my_view', my_view, name = 'my_view'),
    path('neuro_grafico', neuro_grafico, name = 'neuro_grafico'),
]


