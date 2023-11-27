from daos.dao_abs import DAO
from entidade.partida import Partida

class dao_partida(DAO):
    def __init__(self):
        super().__init__('partidas.pkl')

    def add(self, partida):
        if((partida is not None) and isinstance(partida, Partida) and isinstance(partida.id, int)):
            super().add(partida.id, partida)

    def update(self, partida: Partida):
        if (partida is not None) and isinstance(partida, Partida) and isinstance(partida.id, int):
            super().update(partida.id, partida)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)