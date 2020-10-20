from cadastramento import *
from interface import *

cadastrados = enlistCadastrados()

print(cadastrados)

cadastrados2 = txtTolist('cadastrados.txt')  # converte o txt dos cadastrados em uma lista
cadastrados2.sort()
cadastrados2.append('Voltar')  # adiciona a opção voltar à posição len(cadastrados)

print(cadastrados2)