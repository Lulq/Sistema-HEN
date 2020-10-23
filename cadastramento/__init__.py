import pandas as pd
from interface import *
from os import remove
from plotagem import *



def pelagens(txt=''):
    pelagens = ['Alazão', 'Amarillho', 'Baio', 'Pampa', 'Preta', 'Rosilho', 'Tordilho']
    escolha = menu(pelagens, txt+'Pelagem Principal:')
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
        y = leiaInt(f'Informe a altura de cernelha em cm para o mes {x}: (0 caso não exista.) ')
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


def dropLineTxt(file, animal):
    try:
        f = open(file,'r', encoding='utf8')
        lines = f.readlines()
        f.close()
        f = open('cadastrados.txt','w',encoding='utf8')
        for line in lines:
            if line != animal +'\n':
                f.write(line)
        f.close()
    except:
        print('Algum problema ao excluir o animal da lista de cadastrados!')
    finally:
        print(f'{animal} excluído da lista de cadastrados com sucesso!')
    

def selectAndDropCadastro():
    '''
    Apresenta uma lista de cadastrados e pede pra selecionar um deles para remoção
    '''
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
                    print(f'Dados de {animal} excluídos com sucesso!')
                    dropLineTxt('cadastrados.txt',animal)

                else:
                    break

def dropCadastro(nome):
    '''
    Remove um único cadastro pelo nome
    Exclui tanto o arquivo csv quanto o nome do cadastrados.txt
    '''
    remove(f'arquivo/{nome}.csv')
    print(f'Dados de {nome} excluídos com sucesso!')
    dropLineTxt('cadastrados.txt',nome)
    


def enlistCadastrados():
    cadastrados = txtTolist('cadastrados.txt')  # converte o txt dos cadastrados em uma lista
    cadastrados = sorted(cadastrados)
    cadastrados.append('Voltar')  # adiciona a opção voltar à posição len(cadastrados)
   
    return cadastrados

       
def nomeEscolhido(animalnum, listacadastrados):
    for indice, valor in enumerate(listacadastrados):  # gira a lista de cadastrados pra pegar o nome do arquivo
                        # a ser lido
        if animalnum == indice + 1:
            animal = valor
            dados = pd.read_csv(f'arquivo/{animal}.csv')
    return animal, dados

def getData(dados):
    nome = dados["nome"][0]
    nascimento = dados["dnasc"][0]
    pelagem = dados["pelagem"][0]
    sexo = dados["sexo"][0]
    altura = dados["medidas"].max()

    return nome, nascimento, pelagem, sexo, altura
    

def showData(dados):
    print(f'Nome: {dados["nome"][0]:>36}')
    print(f'Nascimento: {dados["dnasc"][0]:>30}')
    print(f'Pelagem: {dados["pelagem"][0]:>33}')
    print(f'Sexo: {dados["sexo"][0]:>36}')
    print(f'Altura: {dados["medidas"].max():>32}cm')

def alterName(df,item):
    selecionado = str(df[item][0])
    df.nome = str(input('Novo nome: '))
    print(f'Nome alterado para {df[item][0]}')
    while True:
        resp = menu(['Sim','Não'], 'Deseja Confirmar a mudança?')
        if resp == 1:
            del df['Unnamed: 0']
            df.to_csv(f'arquivo/{df["nome"][0]}.csv')
            addtocadastrados('cadastrados.txt', f'{df["nome"][0]}' )
            dropCadastro(selecionado)
            break
        else:
            break

def alterItem(df,item,dado):
    df[item] = dado
    del df['Unnamed: 0']
    df.to_csv(f'arquivo/{df["nome"][0]}.csv')
    
def insertAltura(animal,mes,medida):

    colect = []
    labels = open(f'arquivo/{animal}.csv','r').readline().strip().split(',') #pega os labels das colunas e bota em uma lista
    #cria uma lista de dicionários com todos os dados do csv
    with open(f'arquivo/{animal}.csv', 'r') as dados:
        for dado in dados.readlines():
            d = dado.strip().replace('\n','')
            d_lista = d.split(",")
            animal_dict = {}
            for indice, valor in enumerate(d_lista):
                animal_dict[labels[indice]] = valor
            colect.append(animal_dict)

    del colect[0] #elimina a primeira linha que contem apenas labels
    primedic = colect[0] # pega o primeiro dicionário da lista de dicionários para servir de modelo de dicionário
    del primedic['']
    #cria duas listas para armazenar os meses informados e as alturas desses meses
    listaDeMeses = []  
    listaDeAlturas = []
    #roda um loop do tamanho da quantidade de dicionários da grande lista que é definida pela quantidade de meses informados
    for i in range(len(colect)):
        listaDeMeses.append(i) #adiciona os índices a lista de meses informados 
        alt = colect[i].get('medidas') #pega as alturas informadas em cada mês informado
        listaDeAlturas.append(int(alt)) #adiciona as alturas a lista de Alturas
    
    #adição dos dados informados (adicionar verificação depois)
    listaDeMeses.append(mes) 
    listaDeAlturas.append(medida)
    
    #adiciona as listas ao dicionário modelo
    primedic['meses informados'] = listaDeMeses
    primedic['medidas'] = listaDeAlturas
    
    remove(f'arquivo/{animal}.csv') #remove versão anterior do csv
    df = pd.DataFrame(primedic) #transforma o dicionário em dataframe
    df.to_csv(f'arquivo/{df["nome"][0]}.csv') #salva o dataframe atualizado com a nova medida


    

    

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
        a = open(arq, 'at', encoding='utf8')
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


def savetocsv(dicionario):
    '''
    Recebe um dicionário como parâmetro e converte pra arquivo .csv
    '''
    df = pd.DataFrame(dicionario) #transforma o dicionário em dataframe
    df.to_csv(f'arquivo/{df["nome"][0]}.csv') #salva o dataframe com o nome do animal
    addtocadastrados('cadastrados.txt',nome=df["nome"][0]) #inclui o nome do animal no arquivo cadastrados.txt

    return df

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





