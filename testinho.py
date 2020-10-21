from cadastramento import *

cadastrados, animal, dados = showCadastrados()

print(cadastrados)
print()
print(animal)
print()
print(dados)

#   continuação da função showdata
 '''

              
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
    return animal, dados'''