import matplotlib.pyplot as plt
import pandas as pd


def plotindividual(csv):
    plt.plot(csv['meses informados'],csv['medidas'],label=csv['nome'][0].split(' ')[0],marker='o')
    plt.title(csv['nome'][0])
    plt.ylabel('Altura de cernelha(cm)')
    plt.xlabel('Idade(meses)')

def plotxpadrões(csv,male=True,female=True):
    maleref = [93.47550000000001, 102.414, 108.3225, 113.4735, 117.26100000000001, 120.4425, 122.8665, 124.836,
               126.957, 128.6235, 130.7445, 131.9565, 133.32, 133.92600000000002, 134.53199999999998, 135.138,
               135.744, 136.35, 136.95600000000002, 137.56199999999998, 138.168, 138.774, 139.38, 140.1375,
               140.7435, 146.955, 149.83350000000002, 151.5]
    femaleref = [92.904, 101.57699999999998, 107.604, 113.043, 116.13, 119.21699999999998, 121.569, 124.215,
                 125.53800000000001, 127.74300000000001, 129.948, 130.68300000000002, 132.15300000000002, 132.1824,
                 132.1971, 132.2265, 132.2412, 132.2706, 132.3, 133.035, 133.77, 134.505, 135.24, 135.975, 136.71,
                 142.443, 145.53, 147.0]
    indiceidade = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 36, 48, 60]


    if male:
        plt.plot(indiceidade, maleref,label='Machos')
    if female:
        plt.plot(indiceidade,femaleref,label='Fêmeas')
    elif male and female:
        plt.plot(indiceidade, femaleref,label='Fêmeas')
        plt.plot(indiceidade, maleref, label='Machos')

    plotindividual(csv)
    plt.legend(loc="best")

    return plt.show()

def plotXplot(a,b):
    bplt = pd.read_csv(f'arquivo/{b}.csv')
    plotindividual(a)
    plotindividual(bplt)
    plt.title(f'{a["nome"][0]} x {b}')
    plt.legend(loc='best')
    return plt.show()

def plotDic(dic,animal):
    plt.plot(list(dic.keys()), list(dic.values()),label='Crescimento simulado',marker='o',color='blueviolet') #TODO mudar nome do label
    plt.title(f'{animal} (Simulação)')
    plt.ylabel('Altura de cernelha(cm)')
    plt.xlabel('Idade(meses)')
    
def plotDicxpadrões(dic,animal,df):
    maleref = [93.47550000000001, 102.414, 108.3225, 113.4735, 117.26100000000001, 120.4425, 122.8665, 124.836,
               126.957, 128.6235, 130.7445, 131.9565, 133.32, 133.92600000000002, 134.53199999999998, 135.138,
               135.744, 136.35, 136.95600000000002, 137.56199999999998, 138.168, 138.774, 139.38, 140.1375,
               140.7435, 146.955, 149.83350000000002, 151.5]
    femaleref = [92.904, 101.57699999999998, 107.604, 113.043, 116.13, 119.21699999999998, 121.569, 124.215,
                 125.53800000000001, 127.74300000000001, 129.948, 130.68300000000002, 132.15300000000002, 132.1824,
                 132.1971, 132.2265, 132.2412, 132.2706, 132.3, 133.035, 133.77, 134.505, 135.24, 135.975, 136.71,
                 142.443, 145.53, 147.0]
    indiceidade = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 36, 48, 60]


   
    
    plt.plot(indiceidade, femaleref,label='Fêmeas',color='pink',zorder=1)
    plt.plot(indiceidade, maleref, label='Machos',color='paleturquoise',zorder=2) #lightcyan
   
    plotDic(dic,animal)
    
    plt.scatter(df['meses informados'],df['medidas'], label='Medidas reais',marker='o',color='orange',zorder=4)
    
    plt.legend(loc="best")

    return plt.show()