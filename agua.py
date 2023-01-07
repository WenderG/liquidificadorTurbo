from abc import ABC, abstractmethod


class AguaInterface(ABC):
    def __init__(self, quantidade):
        self.quantidade = quantidade

    @abstractmethod
    def pegou_a_agua(self, quantidade) -> bool:
        if quantidade >= 0.25:
            return bool(True)
        else:
            return bool(False)



