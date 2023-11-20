import time
from controle.controladorOceano import ControladorOceano
from controle.controladorJogador import ControladorJogador
from controle.controladorPartida import ControladorPartida
from controle.controlador_barco_super import ControladorBarcoSuper
from controle.controladorRodada import ControladorRodada
from controle.controladorSuperplayer import ControladorSuperPlayer
from limite.telaSistema import TelaSistema
from limite.telaPartida import TelaPartida
from limite.telaJogador import TelaJogador
from limite.telaRodada import TelaRodada


class ControladorSistema():
    def __init__(self):
        self.__controlador_barco_super = ControladorBarcoSuper(self)
        self.__controlador_jogador = ControladorJogador(self)
        self.__controlador_oceano = ControladorOceano(self)
        self.__controlador_partida = ControladorPartida(self)
        self.__controlador_rodada = ControladorRodada(self)
        self.__controlador_super_player = ControladorSuperPlayer(self)
        self.__tela_sistema = TelaSistema()
        self.__tela_partida = TelaPartida()
        self.__tela_jogador = TelaJogador()
        self.__tela_rodada = TelaRodada()

    @property
    def controlador_rodada(self):
        return self.__controlador_rodada

    @property
    def controlador_jogador(self):
        return self.__controlador_jogador

    @property
    def controlador_barco_super(self):
        return self.__controlador_barco_super

    @property
    def controlador_oceano(self):
        return self.__controlador_oceano

    @property
    def controlador_partida(self):
        return self.__controlador_partida

    @property
    def controlador_super_player(self):
        return self.__controlador_super_player

    @property
    def tela_partida(self):
        return self.__tela_partida

    @property
    def tela_oceano(self):
        return self.__tela_oceano

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    @property
    def tela_jogador(self):
        return self.__tela_jogador

    @property
    def tela_rodada(self):
        return self.__tela_rodada

    def inicializa_sistema(self):
        self.tela_inicial()

    def cadastra_jogador(self):
        self.__controlador_jogador.abre_tela()

    def cadastra_partida(self):
        self.__controlador_partida.abre_tela()

    def encerra_sistema(self):
        self.__tela_sistema.mostra_msg('Encerrando sistema')
        time.sleep(2)
        self.__tela_sistema.mostra_msg('...')
        time.sleep(2)
        self.__tela_sistema.mostra_msg('Sistema encerrado')
        exit(0)
        
    def tela_inicial(self):
        lista_opcoes = {1: self.abre_tela, 0:self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_inicial()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_jogador, 2: self.cadastra_partida,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()