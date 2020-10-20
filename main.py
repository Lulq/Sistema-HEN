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
                select = selectCadastro(cadastrados) #número do animal escolhido
                if select == len(cadastrados): #opção voltar
                    break
                else:
                    showData(select, cadastrados)

            
        
        elif resposta == 3:
            dropCadastro()

        elif resposta == 4:
            print('Volte sempre, até logo!')
            break

    break

# andy = pd.read_csv('Andrômeda do Estrela Negra.csv')


# plotxpadrões(andy)
