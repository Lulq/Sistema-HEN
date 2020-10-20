import pandas as pd
from interface import *
from os import remove



def pelagens():
    pelagens = ['Alazão', 'Amarillho', 'Baio', 'Pampa', 'Preta', 'Rosilho', 'Tordilho']
    escolha = menu(pelagens, 'Pelagem Principal:')
    for i, v in enumerate(pelagens):
        if escolha == i+1:
            prim = pelagens[i]
            if prim == 'Pampa' or prim == 'Rosilho' or prim == 'Tordilho':
                escolha2 = menu(pelagens, f'Pelagem secundária - ({prim} de..)')
                for i, v in enumerate(pelagens):
                    if escolha2 == i+1:
                        sec = pelagens[i]
    if escolha not in (4,6,7):
        return prim.lower()
    if escolha == escolha2:
        return prim.lower()
    else:
        return (prim+' de '+sec).lower()


def cadastrar():
    '''
    Coleta todos os dados do animal
    '''
    lista = []
    indice = []
    cadastro = {'nome': input('Nome: '), 'dnasc': leiaData('Dia-Mês-Ano de nascimento: '),
                'sexo': leiaSexo('Sexo: '), 'pelagem': pelagens(), 'meses informados': indice, 'medidas': lista}
    atual = leiaInt('Com quantos meses de idade foi registrada a última medição? ')  # usar datetime pra calcular automaticamente
    for x in range(atual + 1):
        y = leiaFloat(f'Informe a altura de cernelha em cm para o mes {x}: (0 caso não exista.) ')
        if y > 0:
            lista.append(y)
            indice.append(x)

    print(cadastro)
    return cadastro

def novoCadastro():
    '''
    salva novo cadastro
    '''
    cabeçalho('NOVO CADASTRO')
    recip = cadastrar()
    resp1 = menu(['Salvar dados?', 'Descartar e voltar'], 'SALVAR')
    while True:
        if resp1 == 1:
            savetocsv(recip)
            break
        elif resp1 == 2:
            break

def dropCadastro():
    cadastrados = txtTolist('cadastrados.txt')  # converte o txt dos cadastrados em uma lista
    cadastrados.sort()
    cadastrados.append('Voltar')  # adiciona a opção voltar à posição len(cadastrados)
    while True:
        resp2 = menu(cadastrados, 'EXCLUIR CADASTRO')  # menu com a lista de animais + voltar
        if resp2 == len(cadastrados):
            break
        for indice, valor in enumerate(cadastrados):  # gira a lista de cadastrados pra pegar o nome do arquivo
                    # a ser lido
            if resp2 == indice + 1:
                animal = valor
                confirm = menu(['Sim','Não'], f'DESEJA REALMENTE EXCLUIR {animal}?')
                if confirm == 1:
                    dados = remove(f'arquivo/{animal}.csv')
                    print(f'{animal} excluído com sucesso.')
                else:
                    break

  




def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def addtocadastrados(arq, nome='desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro {nome} adicionado.')
            a.close()


def savetocsv(cadastro):
    global cadastrados
    df = pd.DataFrame(cadastro)
    df.to_csv(f'arquivo/{df["nome"][0]}.csv')
    addtocadastrados('cadastrados.txt',nome=df["nome"][0])

    return df



def txtTolist(nome):
    try:
        a = open(nome,'rt')   # abre o arquivo no modo de leitura
    except:
        print('ERRO ao ler o arquivo')
    else:
        cadastrados = [] #cria uma lista onde serão inseridos os dados das linhas do arquivo
        for linha in a:
            dado = linha.split('\n') # separa os dados por quebra de linha '\n'
            cadastrados.append(dado[0]) # especifica que somente o escrito sera inserido na lista ([0])
    finally:
        return cadastrados  # retorna a lista criada
        a.close()  # fecha o arquivo



def lerArquivo(nome): # inutilizada
    '''
    Ler um arquivo mostrando um menu com suas linhas, retorna o número da linha escolhida.
    :param nome: Nome do Arquivo a ser lido
    :return: a linha escolhida
    '''
    try:
        a = open(nome,'rt')   # abre o arquivo no modo de leitura
    except:
        print('ERRO ao ler o arquivo')
    else:
        cadastrados = [] #cria uma lista onde serão inseridos os dados das linhas do arquivo
        for linha in a:
            dado = linha.split('\n') # separa os dados por quebra de linha '\n'
            cadastrados.append(dado[0]) # especifica que somente o escrito sera inserido na lista ([0])
        lista_escolha = menu(cadastrados, 'ANIMAIS CADASTRADOS') #cria o menu com os dados da lista

        #print(a.read()) #le o arquivo inteiro como tá no original
        #print(a.readlines()) #pega as linhas do arquivo e bota numa lista
    finally:
        return lista_escolha # retorna o número da linha escolhida
        a.close() # fecha o arquivo





