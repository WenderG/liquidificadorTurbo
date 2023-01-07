from fruta import Fruta


class Faz0Suco(Fruta):
    def __init__(self, fruta, l_agua, qnt_gelo):
        super().__init__(fruta)
        self.__l_agua = l_agua
        self.__qnt_gelo = qnt_gelo
        print("\n")
        print("vruuuuuuuuuuuuuu")
        print("BIP")
        print("Seu suco está pronto!")
