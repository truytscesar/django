from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
import datetime
from .models import MyModelDateHj
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
from .models import MyModelDateHj2


from django.shortcuts import redirect
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyModelDateHj2

@csrf_exempt
def semi(request):
    if request.method == 'POST':
        date = MyModelDateHj2.objects.create()
        return render(request, 'app_deteriora/acao_registrada.html')
    return render(request, 'app_deteriora/semi.html')


def my_view(request):
    my_objects = MyModelDateHj2.objects.all()
    return render(request, 'app_deteriora/my_template.html', {'my_objects': my_objects})
