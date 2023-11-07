from abc import abstractmethod, ABC

class Player(ABC):
    @abstractmethod
    def __init__(self):
        self.__fezcerto = False
        
    @property
    def fezcerto(self):
        return self.__fezcerto
    
    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @fezcerto.setter
    def fezcerto(self, fezcerto):
        self.__fezcerto = fezcerto
        
