from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import ( semi, acao_registrada,
)

urlpatterns = [
    path('semi', semi, name = 'semi'),
    path('acao_registrada', acao_registrada, name='acao_registrada'),
]


