from entidade.partida import Partida
from controle.controlador_barco_super import ControladorBarcoSuper
import random
from datetime import date
from daos.dao_partida import dao_partida
from entidade.bote import Bote
from entidade.submarino import Submarino
from entidade.fragata import Fragata
from entidade.portaavioes import Portaavioes
from limite.telaPartida import TelaPartida
from entidade.computador import Computador

class ControladorPartida():
    def __init__(self, controlador_sistema):
        self.__dao_partida = dao_partida()
        self.__tela_partida = TelaPartida()
        self.__controlador_sistema = controlador_sistema
        self.__aux_jog = []
        self.__aux_comp = []
    
    @property
    def aux_jog(self):
        return self.__aux_jog
    
    @property
    def aux_comp(self):
        return self.__aux_comp
    
    @property
    def dao_partida(self):
        return self.__dao_partida
    
    @aux_jog.setter
    def aux_jog(self, aux_jog):
        self.__aux_jog = aux_jog
        
    @aux_comp.setter
    def aux_comp(self, aux_comp):
        self.__aux_comp = aux_comp
    
    def partidas(self):
        partidas = []
        for partida in self.__dao_partida.get_all():
            partidas.append(partida)
        return partidas

    def pega_partida_por_id(self, id:int):
        for partida in self.partidas():
            if partida.id == id:
                return partida
        return None
            
    def nova_partida(self):
        if self.__controlador_sistema.controlador_jogador.jogadores()==[]:
            self.__tela_partida.pop_up('Sem jogadores cadastrados')
        else:
            jogador = self.__controlador_sistema.controlador_jogador.pega_jogador()
            
            if (jogador is not None):

                auxidpar = random.randint(1,2000000)
                auxtimepar = date.today()
                auxoceanopar = self.__controlador_sistema.controlador_oceano.cria_oceano()
                if auxoceanopar == None:
                    return
                lista_barcos = self.__controlador_sistema.controlador_barco_super.listar_barcos()
                lista_barcos_comp = self.__controlador_sistema.controlador_barco_super.listar_barcos()

                pcoceano = auxoceanopar.oceano.copy()
                pcbarcos = lista_barcos.copy()
                auxcomppart = self.__controlador_sistema.controlador_super_player.cria_computador(pcoceano, pcbarcos)

                partida = Partida(auxidpar, auxtimepar, jogador, auxcomppart, auxoceanopar, lista_barcos, lista_barcos_comp)
                self.__dao_partida.add(partida)
                
                auxoceanopar = auxoceanopar.oceano
                
                
                self.__controlador_sistema.tela_partida.mostrar_ordem_posicionamento()
                self.__controlador_sistema.controlador_barco_super.adicionar_posicao(auxoceanopar, lista_barcos)
                self.__controlador_sistema.controlador_barco_super.adicionar_posicao_comp(auxoceanopar , lista_barcos_comp)

                ############# HACK DAS POSIÇOES #######################################

                for cheat in partida.lista_barcos_comp:
                    for poscheat in cheat.posicoes:
                        print ('linha:', poscheat[0]+1, 'coluna', poscheat[1]+1)
                
                ###################################################################################
            

                ###################################################################################
                self.__controlador_sistema.tela_partida.compos()
                self.partida_total(partida)

                jogador.add_partida(partida)

                
            else:
                return

    def lista_partidas(self):
        partidas = []
        if len(self.partidas())==0:
            self.__tela_partida.sem_partidas()
        else:
            for partida in self.partidas():
                partidas.append([partida.id, partida.jogador.nome, partida.data_hora, len(partida.rodadas), partida.vencedor])
                
            self.__tela_partida.mostra_partidas(partidas)
                

    def buscar_partida(self):
        partidas = []
        if len(self.partidas())==0:
            self.__tela_partida.sem_partidas()
        else:
            for partida in self.partidas():
                partidas.append(partida.id)
                
            id_partida = self.__tela_partida.pega_partida(partidas)
            if id_partida != None:
                
                partida = self.pega_partida_por_id(id_partida)
                
                for partidaa in self.partidas():
                    print(partidaa.id)
                    print(partida)
                    if partidaa.id == partida.id:
                        aux = self.__tela_partida.mostra_partida_sozinha(partida.id, partida.jogador.nome, partida.data_hora, len(partida.rodadas), partida.vencedor, partida.rodadas)
                        
                if aux == 0:
                    rodadas = []
                    for rodada in self.__controlador_sistema.controlador_rodada.rodadas:
                        if rodada in partida.rodadas:
                            rodadas.append(rodada)
                            
                    self.__controlador_sistema.controlador_rodada.lista_rodadas(rodadas)
            
            

            
    def excluir_partida(self):
        partidas = []
        if len(self.partidas())==0:
            self.__tela_partida.sem_partidas()
        else:
            partidas = []
            for partida in self.partidas():
                partidas.append(partida.id)
                
            id_partida = self.__tela_partida.pega_partida(partidas)
            partida = self.pega_partida_por_id(id_partida)
            
            if partida is not None:
                #arrumar pontuação 
                pontos = 0
                for rodada in partida.rodadas:
                    pontos += rodada.pontos_jog
                
                jogador = partida.jogador
                jogador.pontuacao = jogador.pontuacao - pontos
                self.__controlador_sistema.controlador_jogador.dao_jogador.update(jogador)
                self.__dao_partida.remove(partida.id)
                self.__tela_partida.pop_up('Partida excluída com sucesso')


    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def add_barco(self, lista_barco):
        self.__lista_barco.append(lista_barco)

    def abre_tela(self):
        lista_opcoes = {1: self.nova_partida, 2: self.lista_partidas, 3: self.buscar_partida, 4: self.excluir_partida, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_partida.tela_opcoes()]()
            
    def partida_total(self, partida):

        while True:
            
            if all(not barco.estado for barco in partida.lista_barcos_comp):
                self.__tela_partida.fimpartida(True)
                jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_por_id(partida.jogador.id)
                #jogador.pontuacao += 56 #alterar dps
                partida.vencedor = jogador.nome
                self.__dao_partida.update(partida)
                break

            aux = self.__controlador_sistema.controlador_rodada.rodada(partida)
            
            if all(not barco.estado for barco in partida.lista_barcos_comp):
                self.__tela_partida.fimpartida(True)
                jogador = self.__controlador_sistema.controlador_jogador.pega_jogador_por_id(partida.jogador.id)
                #jogador.pontuacao += 56 #alterar dps
                partida.vencedor = jogador.nome
                rodada = self.__controlador_sistema.controlador_rodada.rodada_total(aux, 0, partida.jogador)
                partida.rodadas.append(rodada)
                self.__dao_partida.update(partida)
                break
            
            if all(not barco.estado for barco in partida.lista_barcos):
                self.__tela_partida.fimpartida(False)
                partida.vencedor = 'computador'
                self.__dao_partida.update(partida)
                break

            aux_comp = self.__controlador_sistema.controlador_rodada.rodada_comp(partida)
            rodada = self.__controlador_sistema.controlador_rodada.rodada_total(aux, aux_comp, partida.jogador)
            
            partida.rodadas.append(rodada)
            
            
            if all(not barco.estado for barco in partida.lista_barcos):
                self.__tela_partida.fimpartida(False)
                partida.vencedor = 'computador'
                rodada = self.__controlador_sistema.controlador_rodada.rodada_total(aux, aux_comp, partida.jogador)
                partida.rodadas.append(rodada)
                self.__dao_partida.update(partida)
                break


        
            
            
        

    

