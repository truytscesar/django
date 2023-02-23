from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect



# Create your views here.
def semi(request):
    return render(request, 'app_deteriora/semi.html')

def acao_registrada(request):
    return render(request, 'app_deteriora/acao_registrada.html')


from django.http import JsonResponse


'''
    result = "Ação salva com sucesso" 
    return JsonResponse({'result': result})
'''