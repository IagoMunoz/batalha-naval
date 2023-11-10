from entidade.superplayer import Player


class Jogador(Player):
    def __init__(self, id, nome, data_nascimento):
        super().__init__()
        self.__id = id
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__pontuacao = 0
        self.__partidas = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao

    @property
    def partidas(self):
        return self.__partidas

    def add_partida(self, partida):
        auxpont = partida.pontos
        self.__pontuacao += auxpont
        self.__partidas.append(partida)