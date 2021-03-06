from plotagem import *
from simulador import *


#desenvolvendo predição de crescimento

#indices de meses e porcentagens de altura expandidos
animal = 'Bruma do Estrela Negra'
dados = pd.read_csv(f'arquivo/{animal}.csv')

indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17, 18,19,20,21,22,23, 24, 36, 48, 60]
machox = [61.7, 67.6, 71.5, 74.9, 77.4, 79.5, 81.1, 82.4, 83.8, 84.9, 86.3, 87.1, 88.0, 88.4, 88.8, 89.2, 89.6, 90,
          90.4, 90.8, 91.2, 91.6, 92, 92.5, 92.9, 97.0, 98.9, 100]
femeax = [63.2, 69.1, 73.2, 76.9, 79.0, 81.1, 82.7, 84.5, 85.4, 86.9, 88.4, 88.9, 89.9, 89.92, 89.93, 89.95, 89.96,
          89.98, 90.0, 90.5, 91, 91.5, 92, 92.5, 93.0, 96.9, 99.0, 100]


dicMacho = {0: 61.7, 1: 67.6, 2: 71.5, 3: 74.9, 4: 77.4, 5: 79.5, 6: 81.1, 7: 82.4, 8: 83.8, 9: 84.9, 10: 86.3, 11: 87.1, 12: 88.0, 13: 88.4, 14: 88.8, 15: 89.2, 16: 89.6, 17: 90, 18: 90.4, 19: 90.8, 20: 91.2, 21: 91.6, 22: 92, 23: 92.5, 24: 92.9, 36: 97.0, 48: 98.9, 60: 100}

dicFemea = {0: 63.2, 1: 69.1, 2: 73.2, 3: 76.9, 4: 79.0, 5: 81.1, 6: 82.7, 7: 84.5, 8: 85.4, 9: 86.9, 10: 88.4, 11: 88.9, 12: 89.9, 13: 89.92, 14: 89.93, 15: 89.95, 16: 89.96, 17: 89.98, 18: 90.0, 19: 90.5, 20: 91, 21: 91.5, 22: 92, 23: 92.5, 24: 93.0, 36: 96.9, 48: 99.0, 60: 100} 


gerado = gerarAlturas(dados)
print(f'Curva de crescimento simulada: {gerado}')


plotDicxpadrões(gerado,animal,dados)