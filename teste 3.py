from cadastramento import *
from interface import *


df = pd.read_csv('arquivo/Grego.csv')

def alterItems(df,item):
    selecionado = str(df[item][0])
    df[item] = input('Novo nome: ')
    print(f'Nome alterado para {df[item][0]}')
    while True:
        resp = menu(['Sim','Não'], 'Deseja Confirmar a mudança?')
        if resp == 1:
            df.to_csv(f'arquivo/{df["nome"][0]}.csv')
            addtocadastrados('cadastrados.txt', f'{df["nome"][0]}' )
            dropCadastro(selecionado)
            break
        else:
            break

alterItems(df,'nome')


