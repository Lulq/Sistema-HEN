from cadastramento import *
from interface import *


while True:
    mes = leiaInt('Para qual mês deseja informar a altura? ')
    alt = leiaInt('Qual a altura(em cm)? ')
    resposta = menu(['Sim','Não'], f'{alt} cm aos {mes} meses, confirma?')

    if resposta == 2:
        break
    elif resposta == 1:
        insertAltura('Lula',mes,alt)
        break
