from colorama import init
init()

def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista, txt):
    cabeçalho(txt)
    c = 1
    for item in lista:
        print(f'\033[32m{c} - \033[m\033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mSua opção:\033[m ')
    return opc


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número inteiro válido. \033[m')
            continue
        except (KeyboardInterrupt):  # nao ta funcionando o kI
            print('\n\033[31mO usuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n0 = input(msg).replace(',', '.')
            n = float(n0)
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor digite um número válido. \033[m')
            continue
        except (KeyboardInterrupt):  # nao ta funcionando o kI
            return 0
        else:
            return n


def leiaData(txt):
    while True:
        try:
            data0 = input(txt).replace('/', '-').split(sep='-')
            dia = int(data0[0])
            mes = int(data0[1])
            ano = int(data0[2])

            if dia > 31:
                print(f'Dia {dia} de um mês não existe, tente outra vez.')
            if mes > 12:
                print('Mês inválido, não existe algo tipo "Trezembro", tente de novo!')
            if ano > 2100:
                print('Este não é um sistema de viagem ao futuro. Verifique o ano digitado!')
            if ano < 1970:
                print('Este não é um sistema de verificação de múmias! Corrija o ano e tente outra vez.')
            elif 0 < dia < 32 and 0 < mes < 13 and 1970 < ano < 2100:
                data = f'{dia}-{mes}-{ano}'
                return data
                break

        except:
            print('Erro: Verifique a data informada. Deve estar no formato Dia-Mês-Ano.')


def leiaSexo(txt):
    while True:
        a = input(txt).strip().upper()[0]
        if a in 'MF':
            break
        else:
            print('ERRO! Digite M para Macho ou F para Fêmea.')
    return a

def txtTolist(nome):
    try:
        a = open(nome,'rt', encoding='utf-8')   # abre o arquivo no modo de leitura #adicionado o encoding por problemas de acentuação
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



