import pandas as pd

# Referências
animal = 'Begônia da Santalice'
dados = pd.read_csv(f'arquivo/{animal}.csv')
indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17, 18,19,20,21,22,23, 24, 36, 48, 60]
dicMacho = {0: 61.7, 1: 67.6, 2: 71.5, 3: 74.9, 4: 77.4, 5: 79.5, 6: 81.1, 7: 82.4, 8: 83.8, 9: 84.9, 10: 86.3, 11: 87.1, 12: 88.0, 13: 88.4, 14: 88.8, 15: 89.2, 16: 89.6, 17: 90, 18: 90.4, 19: 90.8, 20: 91.2, 21: 91.6, 22: 92, 23: 92.5, 24: 92.9, 36: 97.0, 48: 98.9, 60: 100}
dicFemea = {0: 63.2, 1: 69.1, 2: 73.2, 3: 76.9, 4: 79.0, 5: 81.1, 6: 82.7, 7: 84.5, 8: 85.4, 9: 86.9, 10: 88.4, 11: 88.9, 12: 89.9, 13: 89.92, 14: 89.93, 15: 89.95, 16: 89.96, 17: 89.98, 18: 90.0, 19: 90.5, 20: 91, 21: 91.5, 22: 92, 23: 92.5, 24: 93.0, 36: 96.9, 48: 99.0, 60: 100} 

def gerarAlturas(df_escolhido):
    ''' Recebe um Dataframe coleta as alturas informadas e gera alturas simuladas para os meses não informados
        retornando um dicionário com alturas para todos os meses índices.
    '''
    
    meses_informados = df_escolhido['meses informados'] 
    medidas = df_escolhido['medidas']
    # Gera o dicionario modelo para ser posteriormente preenchido nas lacunas.
    modelo = {}
    count = 0
    for item in indices:
        if item in meses_informados:
            modelo[item] = medidas[count]
            count += 1
        else:
            modelo[item] = 0
    #Separa em tuplas mes/altura/porcentagem as medidas disponíveis
    tuplaslist = []
    for k,v in modelo.items():
        if v != 0:
            mes = k
            altura = v
            porcentagem = dicFemea[mes]
            tupla = (mes, altura, porcentagem)
            tuplaslist.append(tupla)
    # gerando o valor de referência para 100%
    # lista com as alturas pra 100%(60meses)
    xlist = []
    for item in tuplaslist:
        mes = item[0]
        altura = item[1]
        percentual = item[2]
        x = altura * 100 / percentual
        xlist.append(x)
    # Média calculada para 100% de altura
    xmedio = sum(xlist)/len(xlist)

    #motor que vai preencher todos os dados zerados do dicionário modelo
    for k,v in modelo.items():
        if v == 0:
            modelo[k] = (xmedio * dicFemea[k]/100)
        else:
            pass
    
    # modelo com as alturas simuladas
    return modelo
    
gerado = gerarAlturas(dados)
print(gerado)