from entidade.superplayer import Player


#fazer versao v2 para melhorar a implementacao
class Computador(Player):
    def __init__(self):
        super().__init__()
        
        
        '''@property
        def acertou(self):
            return self.__acertou
        
        @property
        def destruiu(self):
            return self.__destruiu
        
        def ultimos (self, jogada_yx):
            self.__ultimo_y = jogada_xy[0]
            self.__ultimo_x = jogada_xy[1]
            
        #true se acabou de destruir um barco e false se nao
        def destruiu(self, Bool):
            self.__destruiu = Bool
            
        #true se acabou de acertar um barco e false se acabou de errar
        def acertou(self, Bool):
            self.__acertou = Bool
        
        #botar excecao para caso tente atirar fora do oceano
        #botar excecao para caso tente atirar onde ja atirou
        def jogada_random(self):
            jogada_yx=[]
            jogada_yx.append(random.randint(1,oceano.tamanho_y))
            jogada_yx.append(random.randint(1,oceano.tamanho_x))
            self.ultimos(jogada_yx)
            return jogada_yx
        
        #botar excecao para caso tente atirar fora do oceano
        #botar excecao para caso tente atirar onde ja atirou
        def jogada_acerto(self):
            aux_valor=random.randint(1, 4)
            jogada_yx=[]
            
            if aux_valor==1:
                jogada_yx.append(self.__ultimo_y)
                jogada_yx.append(self.__ultimo_x+1)
                
            if aux_valor==2:
                jogada_yx.append(self.__ultimo_y)
                jogada_yx.append(self.__ultimo_x-1)
                
            if aux_valor==3:
                jogada_yx.append(self.__ultimo_y+1)
                jogada_yx.append(self.__ultimo_x)
                
            if aux_valor==4:
                jogada_yx.append(self.__ultimo_y-1)
                jogada_yx.append(self.__ultimo_x)
                
            self.ultimos(jogada_yx)
            return jogada_yx
            
        #aqui é pra ele ver se ta dentro do tamanho do oceano por isso
        #ele importa o oceano mas pra teste vo fazer sem
        @jogada.computador
        def jogada (self):
            if self.__acertou == True:
                if self.__destruiu== True:
                    self.destruiu(False)
                    return (jogada_random(self))
                else:
                    return (jogada_acerto(self))
            else:
                return (jogada_random(self))'''
                
