from limite.telaJogador import TelaJogador
from entidade.jogador import Jogador
from daos.dao_jogador import dao_jogador


class ControladorJogador():
    def __init__(self, controlador_sistema):
        #self.__jogadores = []
        self.__dao_jogador = dao_jogador()
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def jogadores(self):
        jogadores = []
        for jogador in self.__dao_jogador.get_all():
            jogadores.append(jogador.id)
        return jogadores
    
    def pega_jogador_por_id(self, id: int):
        #for jogador in self.__jogadores:
        for jogador in self.__dao_jogador.get_all():
            if(jogador.id == id):
                return jogador
        return None

    def incluir_jogador(self):
        dados_jogador = self.__tela_jogador.pega_dados()
        jogador = Jogador(dados_jogador["id"], dados_jogador["nome"], dados_jogador["data de nascimento"])
        #self.__jogadores.append(jogador)
        self.__dao_jogador.add(jogador)
        self.__controlador_sistema.controlador_super_player.players.append(jogador)

    def alterar_jogador(self):
        jogadores = self.jogadores()
        id_jogador = self.__tela_jogador.seleciona_jogador(jogadores)
        jogador = self.pega_jogador_por_id(id_jogador)

        if (jogador is not None):
            opcao = self.__tela_jogador.mudar_jogador()

            if opcao == 1:
                nome = self.__tela_jogador.alterar_nome()
                jogador.nome = nome

            if opcao == 2:
                data = self.__tela_jogador.alterar_nascimento()
                jogador.data_nascimento = data

        else:
            self.__tela_jogador.mostra_msg('Jogador não encontrado')

    def lista_jogadores(self):
        jogadores = []
        if len(self.__dao_jogador.get_all()) == 0:
            self.__tela_jogador.mostra_jogador(None)

        for jogador in self.__dao_jogador.get_all():
            jogadores.append([jogador.id, jogador.nome, jogador.data_nascimento, jogador.pontuacao])
        self.__tela_jogador.mostra_jogador(jogadores)
        
    def excluir_jogador(self):
        jogadores = []
        for jogador in self.__dao_jogador.get_all():
            jogadores.append(jogador.id)
            
        id_jogador = self.__tela_jogador.seleciona_jogador(jogadores)
        jogador = self.pega_jogador_por_id(id_jogador)

        if (jogador is not None):
            '''for partida in self.__controlador_sistema.controlador_partida.partidas:
                if partida.jogador==jogador:
                    self.__controlador_sistema.controlador_partida.partidas.remove(partida)'''
            self.__dao_jogador.remove(jogador.id)
            self.__tela_jogador.mostra_msg('Jogador excluído com sucesso!')
        else:
            self.__tela_jogador.mostra_msg('Jogador não encontrado')

    def buscar_jogador(self):
        jogadores = []
        partidas = []
        for jogador in self.__dao_jogador.get_all():
            jogadores.append(jogador.id)
        id_jogador = self.__tela_jogador.seleciona_jogador(jogadores)
        jogador = self.pega_jogador_por_id(id_jogador)

        if len(jogador.partidas)==0:
            self.__tela_jogador.mostra_jogador_sozinho(jogador.id, jogador.nome, jogador.data_nascimento, jogador.pontuacao)

        else:
            for partida in self.__controlador_sistema.controlador_partida.partidas:
                if partida.jogador == jogador:
                    partidas.append([partida.id, partida.jogador, partida.data_hora, partida.vencedor])
            self.__tela_jogador.mostra_jogador_sozinho_sem_partida(jogador.id, jogador.nome, jogador.data_nascimento, jogador.pontuacao, partidas)


    def ranking(self):
        jogs = self.__dao_jogador.get_all()
        jogs.sort(key = lambda player: player.pontuacao, reverse = True)

        for player in jogs:
            self.__tela_jogador.ranking(f'{player.nome} Pontuação: {player.pontuacao}')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.lista_jogadores, 4: self.excluir_jogador, 5: self.buscar_jogador, 6:self.ranking, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_jogador.tela_opcoes()]()