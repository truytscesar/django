    
    #file = open("/static/tbl_teste_.csv")
    #df = csv.reader(file)
    #df = pd.read_csv(open("tbl_teste_.csv"))
    
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
    

    context = {'table_html': table_html}
    return render(request, 'app_deteriora/neuro.html', context)




 form_graficos_neuro = LeitosGraficosForm(request.POST or None)
    dados4 = {}
    dados4['form_graficos_neuro'] = form_graficos_neuro
    
    if form_graficos_neuro.is_valid():
        form_graficos_neuro.save()
        for e in LeitosGraficos.objects.all():
            leito_neuro = e.leitos_graficos_neuro

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
        plt.show()

        return render(request, 'app_deteriora/neuro_grafico.html')
    return render(request, 'app_deteriora/neuro.html',context, dados4)