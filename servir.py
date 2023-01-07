from agua import AguaInterface
from gelo import GeloInterface
from liquidificadorTurbo import Faz0Suco


def copos_de_suco(litros):
    copos = litros / 0.25
    return copos

aux = 0

print("----Fazendo teu suquinho----")

while aux == 0:
    print("\n")
    litros = float(input("Litros de água: "))
    l_agua = AguaInterface.pegou_a_agua(AguaInterface, litros)

    if l_agua:
        print("Água colocada")
        cubos = int(input("Cubos de gelo: "))

        qnt_gelo = GeloInterface.pegou_o_gelo(GeloInterface, cubos)

        sabor = input("Fruta: ")

        pessoa = Faz0Suco(sabor, l_agua, qnt_gelo)

        print("\n")
        print(f'Suco de {sabor}')
        print(f'Quantidade de copos: {copos_de_suco(litros)}')
        print(f'Cubos de gelo: {cubos}')
        print("\n")
        print("Mais suco? 0 - sim | 1 - não")

    else:
        print("Sem água o suficiente!")
        print("Tentar novamente? 0 - sim | 1 - não")

    aux = int(input("Opção: "))
