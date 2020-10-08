from plotagem import *
from interface import *
from cadastramento import *

arq = arquivoExiste('cadastrados.txt')
if not arq:
    criarArquivo('cadastrados.txt')

while True:
    while True:
        resposta = menu(['Cadastrar novo indivíduo', 'Ver animais cadastrados', 'Sair'], 'MENU PRINCIPAL')

        if resposta == 1:
            cabeçalho('NOVO CADASTRO')
            recip = cadastrar()
            resp1 = menu(['Salvar dados?', 'Descartar e voltar'], 'SALVAR')
            while True:
                if resp1 == 1:
                    savetocsv(recip)
                    break
                elif resp1 == 2:
                    break

        elif resposta == 2:
            cadastrados = txtTolist('cadastrados.txt')  # converte o txt dos cadastrados em uma lista
            cadastrados.sort()
            cadastrados.append('Voltar')  # adiciona a opção voltar à posição len(cadastrados)
            while True:
                resp2 = menu(cadastrados, 'ANIMAIS CADASTRADOS')  # menu com a lista de animais + voltar
                if resp2 == len(cadastrados):
                    break
                for indice, valor in enumerate(cadastrados):  # gira a lista de cadastrados pra pegar o nome do arquivo
                    # a ser lido
                    if resp2 == indice + 1:
                        animal = valor
                        dados = pd.read_csv(f'arquivo/{animal}.csv')
                        resp2_x = menu(['Ver dados', 'Plotar crescimento', 'Alterar dados', 'Voltar'], animal)

                if resp2_x == 1:
                    # criar função pra isso
                    print(f'Nome: {dados["nome"][0]:>36}')
                    print(f'Nascimento: {dados["dnasc"][0]:>30}')
                    print(f'Pelagem: {dados["pelagem"][0]:>33}')
                    print(f'Sexo: {dados["sexo"][0]:>36}')
                    print(f'Altura: {dados["medidas"].max():>32}cm')

                elif resp2_x == 2:
                    resp2_x_2 = menu(['Comparar com as médias da raça', 'Comparar outro animal cadastrado',
                                      'Prever crescimento', 'Voltar'], 'Plotar Crescimento')
                    if resp2_x_2 == 1:
                        plotxpadrões(dados)

                    if resp2_x_2 == 2:
                        resp2_x_2_2 = menu(cadastrados, 'Com que animal deseja comparar?')
                        if resp2_x_2_2 == len(cadastrados):
                            break
                        escolhido = cadastrados[resp2_x_2_2 - 1]
                        plotXplot(dados, escolhido)

                    if resp2_x_2 == 4:  # corrigido
                        break
                elif resp2_x == 4:
                    break

        elif resposta == 3:
            print('Volte sempre, até logo!')
            break
    break

# andy = pd.read_csv('Andrômeda do Estrela Negra.csv')


# plotxpadrões(andy)
