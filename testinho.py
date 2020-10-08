import pandas as pd

dadinho = pd.read_csv('arquivo/Andrômeda do Estrela Negra.csv')
print(dadinho)
print()
print(dadinho.head(1)) # 0 não existe, 1 é a primeira linha de indice 0
print()
print(dadinho['nome'][0])
nome = dadinho['nome'][1]

print()
print(f'o nome é {nome}, uma {dadinho["sexo"][0]} de cor {dadinho["pelagem"][0]}, nascida em '
      f'{dadinho["dnasc"][12]} e sua última medição foi {dadinho["medidas"][28]} centímetros')