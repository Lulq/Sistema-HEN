#desenvolvendo predição de crescimento

#indices de meses e porcentagens de altura expandidos

indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17, 18,19,20,21,22,23, 24, 36, 48, 60]
machox = [61.7, 67.6, 71.5, 74.9, 77.4, 79.5, 81.1, 82.4, 83.8, 84.9, 86.3, 87.1, 88.0, 88.4, 88.8, 89.2, 89.6, 90,
          90.4, 90.8, 91.2, 91.6, 92, 92.5, 92.9, 97.0, 98.9, 100]
femeax = [63.2, 69.1, 73.2, 76.9, 79.0, 81.1, 82.7, 84.5, 85.4, 86.9, 88.4, 88.9, 89.9, 89.92, 89.93, 89.95, 89.96,
          89.98, 90.0, 90.5, 91, 91.5, 92, 92.5, 93.0, 96.9, 99.0, 100]


dicMacho = {0: 61.7, 1: 67.6, 2: 71.5, 3: 74.9, 4: 77.4, 5: 79.5, 6: 81.1, 7: 82.4, 8: 83.8, 9: 84.9, 10: 86.3, 11: 87.1, 12: 88.0, 13: 88.4, 14: 88.8, 15: 89.2, 16: 89.6, 17: 90, 18: 90.4, 19: 90.8, 20: 91.2, 21: 91.6, 22: 92, 23: 92.5, 24: 92.9, 36: 97.0, 48: 98.9, 60: 100}

dicFemea = {0: 63.2, 1: 69.1, 2: 73.2, 3: 76.9, 4: 79.0, 5: 81.1, 6: 82.7, 7: 84.5, 8: 85.4, 9: 86.9, 10: 88.4, 11: 88.9, 12: 89.9, 13: 89.92, 14: 89.93, 15: 89.95, 16: 89.96, 17: 89.98, 18: 90.0, 19: 90.5, 20: 91, 21: 91.5, 22: 92, 23: 92.5, 24: 93.0, 36: 96.9, 48: 99.0, 60: 100} 


meses_informados = [3, 5, 7]
medidas = [112, 119, 126 ]

dicAndromeda = {3: 112, 5: 119, 7: 126}


IndicexPercentual= {}
PercentualInd = []
AltxPercentual = {}

'''
for indice, valor in enumerate(meses_informados):
    IndicexPercentual[valor] = dicFemea[valor]
    PercentualInd.append(dicFemea[valor])

for indice, valor in enumerate(medidas):
    AltxPercentual[valor] = PercentualInd[indice]

print(IndicexPercentual)
# {3: 76.9, 5: 81.1, 7: 84.5}
print(AltxPercentual)
# {112: 76.9, 119: 81.1, 126: 84.5}
'''
modelo = {}
count = 0
for item in indices:
    if item in meses_informados:
        modelo[item] = medidas[count]
        count += 1
    else:
        modelo[item] = 0

print(f'aqui está um dicionário com todos os meses disponíveis, os que ja tiverem medição com suas respectivas medidas e os que não com 0 atribuído {modelo}')

#motor que vai gerar as medidas simuladas
tuplaslist = []

for k,v in modelo.items():
    if v != 0:
        mes = k
        altura = v
        porcentagem = dicFemea[mes]
        tupla = (mes, altura, porcentagem)
        tuplaslist.append(tupla)

print(f'Os valores com mes, altura e porcentagem referente disponiveis estao em:{tuplaslist}')

# gerando os valores base
xlist = []
for item in tuplaslist:
    mes = item[0]
    altura = item[1]
    percentual = item[2]
    x = altura * 100 / percentual
    xlist.append(x)

print(f'Esta é a lista com as alturas pra 100%(60meses){xlist}')
xmedio = sum(xlist)/len(xlist)
print(f'A média calculada para 100% de altura é {xmedio}')



#motor que vai preencher todos os dados zerados do dicionário modelo
for k,v in modelo.items():
    if v == 0:
        modelo[k] = (xmedio * dicFemea[k]/100)
    else:
        pass
print(f'o modelo com as alturas simuladas é {modelo}')




