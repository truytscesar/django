from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import ( semi, acao_registrada, my_view, neuro,
)

urlpatterns = [
    path('semi', semi, name = 'semi'),
    path('neuro', neuro, name = 'neuro'),
    path('acao_registrada', acao_registrada, name='acao_registrada'),
    path('my_view', my_view, name='my_view'),
]





