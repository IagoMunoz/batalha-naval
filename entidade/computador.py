from entidade.superplayer import Player
import random
from entidade.barco_super import BS

#fazer versao v2 para melhorar a implementacao
class Computador(Player):
    def __init__(self, oceano , barcos):
        super().__init__()
        self.__oceano = 'compuador'
        self.__barcos = 'inteligente'
        self.__jatiro = []
        #################################3
        self.__recertou = False
        self.__destruindo = False
        self.__destruiu = False
        self.__sentido = False
        self.__ultacerto = False


    @property
    def oceano(self):
        return self.__oceano
    
    @oceano.setter
    def oceano(self, oceano):
        self.__oceano = oceano
    
    @property
    def barcos(self):
        return self.__barcos
    
    @barcos.setter
    def barcos(self, barcos):
        self.__barcos = barcos

    @property
    def jatiro(self):
        return self.__jatiro
    
    def addjatiro(self, tiro):
        self.__jatiro.append(tiro)
    
    @property
    def recertou(self):
        return self.__recertou
    
    @recertou.setter
    def recertou(self, recertou):
        self.__recertou = recertou

    @property
    def destruindo(self):
        return self.__destruindo
    
    @destruindo.setter
    def destruindo(self, destruindo):
        self.__destruindo = destruindo
    
    @property
    def destruiu(self):
        return self.__destruiu
    
    @destruiu.setter
    def destruiu(self, destruiu):
        self.__destruiu = destruiu
    
    @property
    def sentido(self):
        return self.__sentido
    
    @sentido.setter
    def sentido(self, sentido):
        self.__sentido = sentido

    @property
    def ultacerto(self):
        return self.__ultacerto
    
    @ultacerto.setter
    def ultacerto(self, ultacerto):
        self.__ultacerto = ultacerto

    
    ##########################################################
    def joga(self, oceano, jatiro):
        valory = (random.randint(1, (len(oceano))))
        valorx = (random.randint(1, (len(oceano[0]))))
        if len(jatiro)!= 0:
            for tiro in jatiro:
                if tiro[0]==valory and tiro[1]==valorx:
                    valory = (random.randint(1, (len(oceano))))
                    valorx = (random.randint(1, (len(oceano[0]))))
        return (valory, valorx)

    ############################################################

    def joga2(self):
        pass
        