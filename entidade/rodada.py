

class Rodada():
    def __init__(self, coor_jog_jog, coor_jog_comp, pontos_jog, pontos_comp):
        self.__jogada_jog = coor_jog_jog
        self.__jogada_comp = coor_jog_comp 
        self.__pontos_jog = pontos_jog
        self.__pontos_comp = pontos_comp

    @property
    def jogada_jog(self):
        return self.__jogada_jog

    @property
    def jogada_comp(self):
        return self.__jogada_comp

    @property
    def pontos_jog(self):
        return self.__pontos_jog

    @property
    def pontos_comp(self):
        return self.__pontos_comp
    
    @pontos_jog.setter
    def pontos_jog(self, pontos_jog):
        self.__pontos_jog = pontos_jog
        
    @pontos_comp.setter
    def pontos_comp(self, pontos_comp):
        self.__pontos_comp = pontos_comp