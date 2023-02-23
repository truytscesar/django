from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
import datetime
from .models import MyModel
from .forms import VariaveisForm


def acao_registrada(request):
    return render(request, 'app_deteriora/acao_registrada.html')

'''
def semi(request):
    formt = VariaveisForm(request.POST or None)
    if formt.is_valid():
        formt.save()
        return render(request, 'app_deteriora/acao_registrada.html')
    return render(request, 'app_deteriora/semi.html')
'''

from django.shortcuts import render
from .models import MyModelDate
from django.utils import timezone


def semi(request):
    formt = VariaveisForm(request.POST or None)
    if formt.is_valid():
        formt.save()
        return render(request, 'app_deteriora/acao_registrada.html')
    return render(request, 'app_deteriora/semi.html')

def my_view(request):
    my_objects = MyModelDate.objects.all()
    return render(request, 'app_deteriora/my_template.html', {'my_objects': my_objects})

def reg_date(request):
    formt = VariaveisForm(request.POST or None)
    if formt.is_valid():
        formt.save()
        return render(request, 'app_deteriora/acao_registrada.html')
    return render(request, 'app_deteriora/semi.html')
