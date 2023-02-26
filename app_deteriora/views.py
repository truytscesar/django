# Carregar pacotes django
# from django.http import request
# from django.contrib.auth.models import User

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles import finders
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Carregar pacotes python
# import csv

from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt
import os
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# Forms
from .forms import MyUserCreationForm, MyUserCreationForm, DataAtualForm, LeitosGraficosForm

# Models
from .models import DataAtual, LeitosGraficos



# Pagina signup
def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return render(request, 'app_deteriora/signin.html', {'form': form})
    else:
        form = MyUserCreationForm()
    return render(request, 'app_deteriora/signup.html', {'form': form})




# Pagina semi
@login_required
@csrf_exempt
def semi(request):
        form_date = DataAtualForm(request.POST or None)
        dados3 = {}
        dados3['form_date'] = form_date
        if form_date.is_valid():
            form_date.save()
            return render(request, 'app_deteriora/acao_registrada.html')
        return render(request, 'app_deteriora/semi.html',dados3)



@login_required
def my_view(request):
    my_objects = DataAtual.objects.all()
    return render(request, 'app_deteriora/my_template.html', {'my_objects': my_objects})

@login_required
def neuro(request):
    csv_path = finders.find('tbl_teste_.csv')
    df = pd.read_csv(csv_path, sep = ',')

     # Convertendo a variavel para o tipo datetime
    df['exec_dt_tm'] = pd.to_datetime(df['exec_dt_tm'])

    # Renomeando as colunas 
    df = df.rename(columns = {'exec_dt_tm':'data predição', 'prob_norm': 'probabilidade deterioração'})
    
    # Selecionando as colunas desejadas
    df_table = df[['data predição', 'leito', 'probabilidade deterioração']]

    # Dividindo as semis de acordo com os leitos
    df_table['leito_n'] = df_table['leito'].str.split('A').str[1].astype('int')
    df_table_neuro = df_table[df_table['leito_n'] > 873]

    df_table_neuro = df_table_neuro.pivot(index='data predição', columns='leito', values='probabilidade deterioração')
    df_table_neuro = df_table_neuro.fillna('')
    df_table_neuro = df_table_neuro.reset_index()
    nomes = df_table_neuro.columns.to_list()
    dados = df_table_neuro.values
    df_table_neuro = pd.DataFrame(dados, columns=nomes)

    # Selecionando as últimas cincos horas de predição 
    df_table_neuro['dif_dt_pred'] = pd.to_datetime(datetime.now(), format = '%Y-%m-%d %H:%M:%S') - pd.to_datetime(df_table_neuro['data predição'], format = '%Y-%m-%d %H:%M:%S')
    df_table_neuro['dif_dt_pred'] = (df_table_neuro['dif_dt_pred'].dt.days)*3600 + df_table_neuro['dif_dt_pred'].dt.seconds
    df_table_neuro = df_table_neuro[df_table_neuro['dif_dt_pred'] < 18000]
    del df_table_neuro['dif_dt_pred']
        
    # Convert the DataFrame to an HTML table
    table_html = df_table_neuro.to_html(index=False)
    

    dados_table = {'table_html': table_html}
 
    form_graficos_neuro = LeitosGraficosForm(request.POST or None)
    dados_grafico = {}
    dados_grafico['form_graficos_neuro'] = form_graficos_neuro

    if form_graficos_neuro.is_valid():
        form_graficos_neuro.save()
        for e in LeitosGraficos.objects.all():
            leito_neuro = e.leitos_graficos_neuro

        csv_path = finders.find('tbl_teste_.csv')
        df = pd.read_csv(csv_path, sep = ',')

        # Convertendo a variavel para o tipo datetime
        df['exec_dt_tm'] = pd.to_datetime(df['exec_dt_tm'])

        # Renomeando as colunas 
        df = df.rename(columns = {'exec_dt_tm':'data predição', 'prob_norm': 'probabilidade deterioração'})
            
        # Selecionando as colunas desejadas
        df_table = df[['data predição', 'leito', 'probabilidade deterioração']]

        # Dividindo as semis de acordo com os leitos
        df_table['leito_n'] = df_table['leito'].str.split('A').str[1].astype('int')
        df_table_neuro = df_table[df_table['leito_n'] > 873]

        # Selecionando o leito
        leito = 'A877'

        # Selecionado os dados do leito desejado
        df1 = df[df['leito'] == leito]
        df1

        # Seleção das variáveis desejadas
        df1 = df1[['data predição', 'probabilidade deterioração']]

        # Definindo o eixo X do Gráfico 
        df1.index = df1['data predição']
        del df1['data predição']

        # Gráfico da probabilidade de deterioração 
        df1.plot(figsize=(15, 6),marker='o')
        plt.xlabel("Data e hora da predição")
        plt.ylabel("Probabilidade de deterioração (%) ")
        plt.title("Probabilidades de deterioração do leito: {}".format(leito) + " da neuro")
        plt.savefig('my_plot.png')
        return render(request, 'app_deteriora/neuro_grafico.html')

    context = {}
    context.update(dados_table)
    context.update(dados_grafico)

    return render(request, 'app_deteriora/neuro.html',context)

@login_required
def neuro_grafico(request):
    return render(request, 'app_deteriora/neuro_grafico.html')

# Pagina coro
@login_required
def coro(request):
    return render(request, 'app_deteriora/coro.html')
