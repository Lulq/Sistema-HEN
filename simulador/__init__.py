import pandas as pd
import matplotlib.pyplot as plt
from operator import itemgetter


#Referências
indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17, 18,19,20,21,22,23, 24, 36, 48, 60]
dicMacho = {0: 61.7, 1: 67.6, 2: 71.5, 3: 74.9, 4: 77.4, 5: 79.5, 6: 81.1, 7: 82.4, 8: 83.8, 9: 84.9, 10: 86.3, 11: 87.1, 12: 88.0, 13: 88.4, 14: 88.8, 15: 89.2, 16: 89.6, 17: 90, 18: 90.4, 19: 90.8, 20: 91.2, 21: 91.6, 22: 92, 23: 92.5, 24: 92.9, 36: 97.0, 48: 98.9, 60: 100}
dicFemea = {0: 63.2, 1: 69.1, 2: 73.2, 3: 76.9, 4: 79.0, 5: 81.1, 6: 82.7, 7: 84.5, 8: 85.4, 9: 86.9, 10: 88.4, 11: 88.9, 12: 89.9, 13: 89.92, 14: 89.93, 15: 89.95, 16: 89.96, 17: 89.98, 18: 90.0, 19: 90.5, 20: 91, 21: 91.5, 22: 92, 23: 92.5, 24: 93.0, 36: 96.9, 48: 99.0, 60: 100} 

def gerarAlturas(df_escolhido):
    ''' Recebe um Dataframe coleta as alturas informadas e gera alturas simuladas para os meses não informados
        retornando um dicionário com alturas para todos os meses índices.
    '''
    # Meses informados
    meses_informados = df_escolhido['meses informados'].tolist() #.tolist() corrigiu o problema 
    
    #Medidas extraídas para os meses informados
    medidas = df_escolhido['medidas'].tolist()

    # Gera dicionário com meses informados e medidas para esses meses
    dicMesesMedidas = {}
    for i, item in enumerate(meses_informados):
        dicMesesMedidas[item] = medidas[i]
        
    # Gera o dicionario modelo para ser posteriormente preenchido nas lacunas.
    modelo = {}
    for item in indices:
        modelo[item] = 0
    
    #junta 2 dicionários em um com todos os meses e medidas disponíveis + todos os indices sem medidas com 0 como valor
    modelo.update(dicMesesMedidas)
    modelo = dict(sorted(modelo.items(), key=itemgetter(0))) #ordena pelas chaves
    
    
    #Separa em tuplas mes/altura/porcentagem as medidas disponíveis
    tuplaslist = []
    for k,v in modelo.items():
        if v != 0 and k in indices: #pega apenas as alturas que tem porcentagem disponível TODO futuramente adicionar mais índices
            mes = k
            altura = v
            if df_escolhido['sexo'][0] == 'F':
                porcentagem = dicFemea[mes]
            else:
                porcentagem = dicMacho[mes]
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
    indicesDoModelo = list(modelo.keys())
    vant = 0
    
    for k,v in modelo.items(): #TODO encontrar nova referencia, ta dando erro na falta dos indices
    #for i, k in enumerate(indicesDoModelo):
        try:
            if k > 0:
                vant = modelo[k-1] #variável pra pegar o valor anterior #TODO erro tá aqui
            if k < 60:
                vpost = modelo[k+1]
        except: 
            pass
        finally:
            if v == 0:
                if df_escolhido['sexo'][0] == 'F':
                    modelo[k] = (xmedio * dicFemea[k]/100)
                else:
                    modelo[k] = (xmedio * dicMacho[k]/100)
                if modelo[k] < vant: # garante que a curva simulada não mostre alturas menores que as anteriores
                    modelo[k] = vant
                elif modelo[k] > vpost and vpost > 0:
                    modelo[k] = vpost
            else:
                pass
    modelo[60] = xmedio
    vant = 0
    for k, v in modelo.items():
        if v < vant:
            modelo[k] = vant    
        vant = modelo[k]
    # modelo com as alturas simuladas
    return modelo

     