from entidade.superplayer import Player
import random

#fazer versao v2 para melhorar a implementacao
class Computador(Player):
    def __init__(self):
        super().__init__()
        

    def joga(self, oceano, jatiro):
        valory = (random.randint(1, (len(oceano))))
        valorx = (random.randint(1, (len(oceano[0]))))
        if len(jatiro)!= 0:
            for tiro in jatiro:
                if tiro[0]==valory and tiro[1]==valorx:
                    valory = (random.randint(1, (len(oceano))))
                    valorx = (random.randint(1, (len(oceano[0]))))
        return (valory, valorx)