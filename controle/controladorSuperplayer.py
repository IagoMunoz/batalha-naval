from entidade.computador import Computador


class ControladorSuperPlayer():
    def __init__(self, controlador_sistema):
        self.__players = []
        self.__controlador_sistema = controlador_sistema

    @property
    def players(self):
        return self.__players

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def cria_computador(self, oceano, barcos):
        computador = Computador(oceano, barcos)
        self.__players.append(computador)
        return computador