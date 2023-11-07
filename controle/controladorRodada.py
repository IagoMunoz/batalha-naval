from entidade.rodada import Rodada
from limite.telaRodada import TelaRodada
from entidade.partida import Partida
class ControladorRodada():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_rodada = TelaRodada()
        self.__rodadas = []
    

    @property
    def rodadas(self):
        return self.__rodadas
    
    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def tela_rodada(self):
        return self.__tela_rodada
    
    
    def lista_rodadas(self):
        for rodada in self.__rodadas:
            self.__tela_rodada.mostra_rodada({"coordenadas do jogador": rodada.jogada_jog, "coordenadas do computador": rodada.jogada_comp, "pontos do jogador": rodada.pontos_jog, "pontos do computador": rodada.pontos_comp})
    
    def rodada_usuario(self, oceano, barcos):
        self.__controlador_sistema.controlador_partida.aux_jog = []
        auxs = self.__controlador_sistema.tela_rodada.atira(oceano, barcos,  jogadnv=True, acertou=0, tiros=[])
        self.__controlador_sistema.controlador_partida.aux_jog.append(auxs)
        
    def rodada_comp(self, oceano, barcos):
        self.__controlador_sistema.controlador_partida.aux_comp = []
        auxs = self.__controlador_sistema.tela_rodada.atira_comp(oceano, barcos, jogadnv=True, acertou=0, tiros=[])
        self.__controlador_sistema.controlador_partida.aux_comp.append(auxs)
        
    def rodada_total(self):
        
        aux_comp = self.__controlador_sistema.controlador_partida.aux_comp[0]
        aux_jog = self.__controlador_sistema.controlador_partida.aux_jog[0]
        if len(aux_comp)==2 and len(aux_jog)==2:
            rodada = Rodada(self.__controlador_sistema.controlador_partida.aux_jog[0][0], self.__controlador_sistema.controlador_partida.aux_comp[0][0], self.__controlador_sistema.controlador_partida.aux_jog[0][1], self.__controlador_sistema.controlador_partida.aux_comp[0][1])
        elif len(aux_comp)==2:
            rodada = Rodada([self.__controlador_sistema.controlador_partida.aux_jog[0][0], self.__controlador_sistema.controlador_partida.aux_jog[0][1]], self.__controlador_sistema.controlador_partida.aux_comp[0][0], self.__controlador_sistema.controlador_partida.aux_jog[0][2], self.__controlador_sistema.controlador_partida.aux_comp[0][1])
        elif len(aux_jog)==2:
            rodada = Rodada(self.__controlador_sistema.controlador_partida.aux_jog[0][0], [self.__controlador_sistema.controlador_partida.aux_comp[0][0], self.__controlador_sistema.controlador_partida.aux_comp[0][1]], self.__controlador_sistema.controlador_partida.aux_jog[0][1], self.__controlador_sistema.controlador_partida.aux_comp[0][2])
        else:
            rodada = Rodada([self.__controlador_sistema.controlador_partida.aux_jog[0][0], self.__controlador_sistema.controlador_partida.aux_jog[0][1]], [self.__controlador_sistema.controlador_partida.aux_comp[0][0], self.__controlador_sistema.controlador_partida.aux_comp[0][1]], self.__controlador_sistema.controlador_partida.aux_jog[0][2], self.__controlador_sistema.controlador_partida.aux_comp[0][2])
        self.__rodadas.append(rodada)
        return rodada
        
        
        
    
        