from plotagem import *
from interface import *
from cadastramento import *

#checa se o arquivo de cadastros existe, e o cria em caso de negativo

arq = arquivoExiste('cadastrados.txt')
if not arq:
    criarArquivo('cadastrados.txt')


# laço maior - menu principal 

while True:
    #menu principal
    while True:
        resposta = menu(['Cadastrar novo indivíduo', 'Ver animais cadastrados', 'Excluir animal cadastrado', 'Sair'], 'MENU PRINCIPAL')
        # Cadastrar novo indivíduo
        if resposta == 1:
            novoCadastro()

        elif resposta == 2:
            while True:
                cadastrados= enlistCadastrados() #lista de animais cadastrados + voltar
                select = menu(cadastrados, 'ANIMAIS CADASTRADOS') #menu ver animais retorna > número do animal escolhido
                if select == len(cadastrados): #opção voltar
                    break
                elif 0 < select < len(cadastrados):
                    escolhido, df_escolhido = nomeEscolhido(select,cadastrados)
                    while True:
                        resposta2 = menu(['Ver dados', 'Plotar crescimento', 'Alterar dados', 'Voltar'], escolhido)
                        #ver dados
                        if resposta2 == 1:
                            showData(df_escolhido)
                        #plotar crescimento
                        elif resposta2 == 2:
                            while True:
                                resposta3 = menu(['Comparar com as médias da raça', 'Comparar outro animal cadastrado',
                                                   'Prever crescimento', 'Voltar'], 'Plotar Crescimento')
                                if resposta3 == 4:
                                    break

                                elif resposta3 == 1:
                                    plotxpadrões(df_escolhido)

                                elif resposta3 == 2:
                                    resposta4 = menu(cadastrados, 'Com que animal deseja comparar?')
                                    if resposta4 == len(cadastrados):
                                        break
                                    escolhido2 = cadastrados[resposta4 - 1]
                                    plotXplot(df_escolhido, escolhido2)

                        #alterar cadastro
                        elif resposta2 == 3:
                            while True:
                                resposta5 = menu(['Nome','Data de Nascimento', 'Pelagem', 'Sexo','Alturas','Alterar tudo','Excluir animal','Voltar'], f'{escolhido} - DESEJA ALTERAR...')
                                if resposta5 == 8:
                                    break
                                elif resposta5 == 7:
                                    dropCadastro(escolhido)
                                    break
                                elif resposta5 == 6:
                                    novoCadastro() #TODO alterar 

                        #voltar
                        elif resposta2 == 4:
                            break
                        
       
        
        elif resposta == 3:
            selectAndDropCadastro()

        elif resposta == 4:
            print('Volte sempre, até logo!')
            break

    break

# andy = pd.read_csv('Andrômeda do Estrela Negra.csv')


# plotxpadrões(andy)
