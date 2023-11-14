from daos.dao_abs import DAO
from entidade.jogador import Jogador

class dao_jogador(DAO):
    def __init__(self):
        super().__init__('jogadores.pkl')

    def add(self, jogador):
        if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.id, int)):
            super().add(jogador.id, jogador)

    def update(self, jogador):
        if((jogador is not None) and isinstance(jogador, Jogador) and isinstance(jogador.id, int)):
            super().update(jogador.id, Jogador)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)