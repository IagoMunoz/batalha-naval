from entidade.superplayer import Player
import random
from entidade.barco_super import BS
from controle.controlador_barco_super import ControladorBarcoSuper
#fazer versao v2 para melhorar a implementacao
class Computador(Player):
    def __init__(self, oceano , barcos):
        super().__init__()
        self.__oceano = oceano
        self.__barcos = barcos
        self.__jatiro = []
        #################################3
        self.__abar = []
        self.__atbar = False
        self.__pos = [0,1,2,3]
        self.__ultimacerto = False
        self.__sentido = False

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
    @jatiro.setter
    def jatiro(self, jatiro):
        self.__jatiro = jatiro
    @property
    def abar(self):
        return self.__abar
    @abar.setter
    def abar(self, abar):
        self.__abar = abar
    @property
    def atbar(self):
        return self.__atbar
    @atbar.setter
    def atbar(self, atbar):
        self.__atbar = atbar
    @property
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self, pos):
        self.__pos = pos
    @property
    def ultimacerto(self):
        return self.__ultimacerto
    @ultimacerto.setter
    def ultimacerto(self, ultimacerto):
        self.__ultimacerto = ultimacerto
    @property
    def sentido(self):
        return self.__sentido
    @sentido.setter
    def sentido(self, sentido):
        self.__sentido = sentido

#########################################################################

    def repos(self):
        self.pos([0,1,2,3])

    def popos(self, pos):
        self.__pos.pop(pos)

    def limpabar(self):
        for barco in self.__abar:
            if barco.estado==False:
                del barco
        
        if len(self.__abar)==0:
            self.atbar=False
        else:
            self.atbar=self.__abar[0]
            for ultiro in self.__abar[0].posicoes:
                if ultiro[2]==False:
                    self.ultimacerto=ultiro[0], ultiro[1]
    
    def addabar(self,barco):
        self.__abar.append(barco)
    
    def addjatiro(self, tiro):
        self.__jatiro.append(tiro)

####################################

    def destruido(self):
        self.recertou(False)
        self.destruindo(False)
        self.destruiu(False)
        self.sentido(False)
        self.ultacerto(False)
################################################################
    def pegbarco(self, tiro):
        for barcin in self.__barcos:
            for posicao in barcin.posicoes:
                if posicao[0] == tiro[0]-1 and posicao[1] == tiro[1]-1:
                    return barcin
        return False
    ##########################################################
    def joga(self, oceano, jatiro):
        valory = (random.randint(1, (len(oceano))))
        valorx = (random.randint(1, (len(oceano[0]))))
        tiro = (valory, valorx)
        if len(jatiro)!= 0:
            while tiro in jatiro:
                valory = (random.randint(1, (len(oceano))))
                valorx = (random.randint(1, (len(oceano[0]))))
                tiro = (valory, valorx)

        return (valory, valorx)

    ############################################################
    def achasen(self):
        decide=[]

        if self.__ultimacerto[0]-self.__atbar.tamanho > 0:
            decide.append(0)
        if self.__ultimacerto[0]+self.__atbar.tamanho < len(self.oceano):
            decide.append(1)
        if self.__ultimacerto[1]-self.__atbar.tamanhi > 0:
            decide.append(2)
        if self.__ultimacerto[1]+self.__atbar.tamanho < len(self.oceano[0]):
            decide.append(3)

        decide2 = []
        for i in range (4):
            if i in decide and i in self.pos:
                decide2.append(i)
        
        chute = self.popos(random.randint(0,len(decide2)-1))

        if chute == 0:
            return ( self.__ultimacerto[0]-1, self.__ultimacerto[1])
        
        if chute == 1:
            return ( self.__ultimacerto[0]+1, self.__ultimacerto[1])
        
        if chute == 2:
            return ( self.__ultimacerto[0], self.__ultimacerto[1]-1)
        
        if chute == 3:
            return ( self.__ultimacerto[0]-1, self.__ultimacerto[1]+1)

    def joga2(self):
        print(self.__jatiro)
        print(self.__ultimacerto)
        print(self.__atbar)

        pass
        if self.__atbar == False:

            tiro = self.joga(self.__oceano, self.__jatiro)
            self.addjatiro(tiro)
            tembar = self.pegbarco(tiro)

            if tembar !=False:
                if tembar.tamanho == 1:
                    ControladorBarcoSuper.tomoutiro(self, self.__barcos, tiro[0], tiro[1])
                    ControladorBarcoSuper.destruido(self.__barcos)
                    self.limpabar()
                    self.__ultimacerto=tiro
                    return (tiro[0], tiro[1])
            
                else:
                    print(tiro)
                    print(self.barcos)
                    print(self.__barcos)
                    ControladorBarcoSuper.tomoutiro(self, self.__barcos, tiro[0], tiro[1])
                    self.addabar(tembar)
                    self.atbar=tembar
                    self.limpabar()
                    self.ultimacerto=tiro
                    return (tiro[0], tiro[1])
            else:
                self.limpabar()
                return (tiro[0], tiro[1])

        elif self.atbar.tamanho == 2:
            tiro = self.achasen
            self.addjatiro(tiro)
            tembar = self.pegbarco(tiro)

            if tembar !=False:
                ControladorBarcoSuper.tomoutiro(self, self.barcos, tiro[0], tiro[1])
                ControladorBarcoSuper.destruido(self.barcos)
                self.limpabar()

                return (tiro[0], tiro[1])
            
            else:
                return (tiro[0], tiro[1])