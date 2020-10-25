from plotagem import *
from interface import *
from cadastramento import *
from simulador import *
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
                                #Voltar
                                if resposta3 == 4:
                                    break
                                #comparar com as médias da raça
                                elif resposta3 == 1:
                                    plotxpadrões(df_escolhido)
                                #comparar com outro animal cadastrado
                                elif resposta3 == 2:
                                    resposta4 = menu(cadastrados, 'Com que animal deseja comparar?')
                                    if resposta4 == len(cadastrados):
                                        break
                                    escolhido2 = cadastrados[resposta4 - 1]
                                    plotXplot(df_escolhido, escolhido2)
                                elif resposta3 == 3:
                                    plotDicxpadrões(gerarAlturas(df_escolhido), escolhido)
                                    break
                                     

                        #alterar cadastro
                        elif resposta2 == 3:
                            while True:
                                resposta5 = menu(['Nome','Data de Nascimento', 'Pelagem', 'Sexo','Adicionar Medição', 'Excluir animal','Voltar'], f'{escolhido} - DESEJA ALTERAR...')
                                #sair
                                if resposta5 == 7:
                                    break
                                #excluir
                                elif resposta5 == 6:
                                    resposta= menu(['Sim','Não'],f'Confirma exclusão de {escolhido}?')
                                    if resposta == 1:
                                        dropCadastro(escolhido)
                                        break
                                    else:
                                        break
                               #alterar nome
                                elif resposta5 == 1:
                                    alterName(df_escolhido,'nome')
                                    break
                                #alterar data
                                elif resposta5 == 2:
                                    newdate = leiaData('Informe a nova data de nascimento:')
                                    alterItem(df_escolhido, 'dnasc', newdate)
                                    print('Data de nascimento atualizada!')
                                    break
                                #alterar pelagem
                                elif resposta5 == 3:
                                    newcolor = pelagens('Nova ')
                                    alterItem(df_escolhido, 'pelagem', newcolor)
                                    print(f'Pelagem alterada para {newcolor}')
                                    break
                                #alterar sexo
                                elif resposta5 == 4:
                                    newsex = leiaSexo('Informe o Sexo[M/F]: ')
                                    alterItem(df_escolhido, 'sexo', newsex)
                                    print(f'Sexo alterado para {newsex}')
                                    break
                                #adicionar altura
                                elif resposta5 == 5:
                                    while True:
                                        mes = leiaInt('Para qual mês deseja informar a altura? ')
                                        alt = leiaInt('Qual a altura(em cm)? ')
                                        resposta = menu(['Sim','Não'], f'{alt} cm aos {mes} meses, confirma?')
                                        if resposta == 2:
                                            break
                                        elif resposta == 1:
                                            insertAltura('Lula',mes,alt)
                                            print(f'Medida:{alt} cm para o mês: {mes} adicionada.')
                                            break
                        #voltar
                        elif resposta2 == 4:
                            break
                        
       
        # Remover animal cadastrado
        elif resposta == 3:
            selectAndDropCadastro()
        # Sair
        elif resposta == 4:
            print('Volte sempre, até logo!')
            break

    break