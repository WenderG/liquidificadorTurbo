from abc import ABC, abstractmethod


class GeloInterface(ABC):
    def __init__(self, quantidade):
        self.quantidade = quantidade

    @abstractmethod
    def pegou_o_gelo(self, quantidade) -> bool:
        if 1 <= quantidade <= 9:
            print("Com gelo")
            return bool(True)
        elif quantidade >= 10:
            print("Com muito gelo")
            print("Geladinho hmmmmmm")
            return bool(True)
        else:
            print("Sem gelo")
            return bool(False)
