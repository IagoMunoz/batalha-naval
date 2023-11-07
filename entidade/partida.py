from controle.controladorSistema import * 
class Partida():
    def __init__(self, id, data_hora, id_jogador, computador, oceano, lista_barcos, lista_barcos_commp):
        self.__id = id
        self.__jogador = id_jogador
        self.__data_hora = data_hora
        self.__rodadas = []
        self.__computador = computador
        self.__oceano = oceano
        self.__vencedor = 0
        self.__pontos = 0
        self.__lista_barcos = lista_barcos
        self.__lista_barcos_comp = lista_barcos_commp
    

    @property
    def id(self):
        return self.__id
    
    @property
    def data_hora(self):
        return self.__data_hora
        
    @property
    def rodadas(self):
        return self.__rodadas
    
    @property
    def jogador(self):
        return self.__jogador
    
    @property
    def computador(self):
        return self.__computador
    
    @property
    def oceano(self):
        return self.__oceano
    
    @property
    def oceano_comp(self):
        return self.__oceano_comp
    
    @property
    def vencedor(self):
        return self.__vencedor
    
    @property
    def pontos(self):
        return self.__pontos
    
    @vencedor.setter
    def vencedor(self, vencedor):
        self.__vencedor = vencedor

    @property
    def id_jogador(self):
        return self.__id_jogador
    
    @property
    def lista_barcos_comp(self):
        return self.__lista_barcos_comp
    
    @property
    def lista_barcos(self):
        return self.__lista_barcos