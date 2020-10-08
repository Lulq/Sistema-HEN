import matplotlib.pyplot as plt


#parte 1 - plotando os gráficos de desenvolvimento segundo o artigo de referência

indice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 24, 36, 48, 60]
macho = [61.7, 67.6, 71.5, 74.9, 77.4, 79.5, 81.1, 82.4, 83.8, 84.9, 86.3, 87.1, 88.0, 90.4, 92.9, 97.0, 98.9, 100]
femea = [63.2, 69.1, 73.2, 76.9, 79.0, 81.1, 82.7, 84.5, 85.4, 86.9, 88.4, 88.9, 89.9, 90.0, 93.0, 96.9, 99.0, 100]

plt.plot(indice,femea, color='red', label='Fêmeas')
plt.plot(indice, macho, label='Machos')
plt.title('Curvas de desenvolvimento segundo estudo da UFRJ')
plt.xlabel('meses')
plt.ylabel('%')
plt.legend(loc='best')
plt.show()

#parte 2 - plotando as curvas de desenvolvimento com dados de preenchimento.
indice2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17, 18,19,20,21,22,23, 24, 36, 48, 60]
machox = [61.7, 67.6, 71.5, 74.9, 77.4, 79.5, 81.1, 82.4, 83.8, 84.9, 86.3, 87.1, 88.0, 88.4, 88.8, 89.2, 89.6, 90,
          90.4, 90.8, 91.2, 91.6, 92, 92.5, 92.9, 97.0, 98.9, 100]
femeax = [63.2, 69.1, 73.2, 76.9, 79.0, 81.1, 82.7, 84.5, 85.4, 86.9, 88.4, 88.9, 89.9, 89.92, 89.93, 89.95, 89.96,
          89.98, 90.0, 90.5, 91, 91.5, 92, 92.5, 93.0, 96.9, 99.0, 100]

plt.plot(indice2, femeax, color='red',label='Fêmeas')
plt.plot(indice2, machox, label='Machos')
plt.title('Curva de desenvolvimento mês a mês, preenchida.')
plt.xlabel('meses')
plt.ylabel('%')
plt.legend(loc='best')
plt.show()

#parte 3 - comparando com dados reais
indiceand = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,21,22,23,24,26,27,28,29,30,33,34,36,48]
andromeda = [92, 103, 107, 112, 116, 119, 122, 126, 126, 129, 129, 130, 132, 132, 133, 133, 137, 139,
             139.5, 140, 140, 142, 143, 145, 146, 146, 146.5, 147, 147, 147]

plt.plot(indiceand,andromeda, color='green', label='Andrômeda')
plt.show()

# parte 4, convertendo porcentagem em altura

from Meus_Programas.crescimento import porcentagemToAltura

curva_cm_macho = porcentagemToAltura(machox)
curva_cm_femea = porcentagemToAltura(femeax, False)

plt.plot(indice2,curva_cm_macho,label="Machos")
plt.plot(indice2,curva_cm_femea,label='Fêmeas')
plt.plot(indiceand,andromeda, marker='o', label='Andrômeda')
plt.title('Comparação de Andrômeda com as curvas referência')
plt.xlabel('meses')
plt.ylabel('Altura em cm')
plt.legend(loc='best')
plt.show()

