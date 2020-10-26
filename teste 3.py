from cadastramento import *
from interface import *
from operator import itemgetter

dicFemea = {0: 63.2, 1: 69.1, 2: 73.2, 3: 76.9, 4: 79.0, 5: 81.1, 6: 82.7, 7: 84.5, 8: 85.4, 9: 86.9, 10: 88.4, 11: 88.9, 12: 89.9, 13: 89.92, 14: 89.93, 15: 89.95, 16: 89.96, 17: 89.98, 18: 90.0, 19: 90.5, 20: 91, 21: 91.5, 22: 92, 23: 92.5, 24: 93.0, 36: 96.9, 48: 99.0, 60: 100}
modelo = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 119.0, 6: 119.0, 7: 121.0, 8: 122.0, 9: 0, 10: 124.0, 11: 126.0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 134.0, 18: 137.0, 19: 138.0, 20: 139.0, 21: 139.0, 22: 139.0, 23: 0, 24: 0, 36: 0, 48: 0, 60: 0}
xmedio = 147

dicA = {0: 92.0, 1: 103.0, 2: 107.0, 3: 112.0, 4: 116.0, 5: 119.0, 6: 122.0, 7: 126.0, 8: 126.0, 9: 129.0, 10: 129.0, 11: 130.0, 12: 132.0, 13: 132.0, 14: 133.0, 15: 133.0, 18: 137.0, 21: 139.0, 22: 139.5, 23: 140.0, 24: 140.0, 26: 142.0, 27: 143.5, 28: 145.0, 29: 146.0, 30: 146.0, 33: 146.5, 34: 147.0, 36: 147.0, 48: 147.0}

dicB = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0, 21: 0, 22: 0, 23: 0, 24: 0, 36: 0, 48: 0, 60: 0}

 #motor que vai preencher todos os dados zerados do dicionário modelo
indicesDoModelo = list(modelo.keys())
vant = 0
    
#for k,v in modelo.items(): #TODO encontrar nova referencia, ta dando erro na falta dos indices
for i, k in enumerate(indicesDoModelo):
       try:
        if k > 0:
            vant = modelo[] #variável pra pegar o valor anterior #TODO erro tá aqui
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
