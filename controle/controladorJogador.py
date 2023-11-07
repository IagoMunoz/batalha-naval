from limite.telaJogador import TelaJogador
from entidade.jogador import Jogador

class ControladorJogador():
    def __init__(self, controlador_sistema):
        self.__jogadores = []
        self.__tela_jogador = TelaJogador()
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    def pega_jogador_por_id(self, id: int):
        for jogador in self.__jogadores:
            if(jogador.id == id):
                return jogador
        return None

    def incluir_jogador(self):
        dados_jogador = self.__tela_jogador.pega_dados()
        jogador = Jogador(dados_jogador["id"], dados_jogador["nome"], dados_jogador["data de nascimento"])
        self.__jogadores.append(jogador)
        self.__controlador_sistema.controlador_super_player.players.append(jogador)

    def alterar_jogador(self):
        id_jogador = TelaJogador.seleciona_jogador(self)
        jogador = self.pega_jogador_por_id(id_jogador)
        
        if (jogador is not None):
            opcao = TelaJogador.alterar_jogador(self)
            if opcao==1:
                nome = TelaJogador.alterar_nome(self)
                jogador.nome = nome
            if opcao==2:
                data = TelaJogador.alterar_nascimento(self)
                jogador.data_nascimento = data
        else:
            self.__tela_jogador.mostra_msg('Jogador não encontrado')
            
        
    def lista_jogadores(self):
        if len(self.__jogadores)==0:
            self.__tela_jogador.mostra_msg('Sem jogadores cadastrados')
        for jogador in self.__jogadores:
            self.__tela_jogador.mostra_jogador({"cod": jogador.id, "nome": jogador.nome, "data de nascimento": jogador.data_nascimento, "pontuação": jogador.pontuacao})
    
    def excluir_jogador(self):
        id_jogador = TelaJogador.seleciona_jogador(self)
        jogador = self.pega_jogador_por_id(id_jogador)
        
        if (jogador is not None):
            '''for partida in self.__controlador_sistema.controlador_partida.partidas:
                if partida.jogador==jogador:
                    self.__controlador_sistema.controlador_partida.partidas.remove(partida)'''
            self.__jogadores.remove(jogador)
            self.__tela_jogador.mostra_msg('Jogador excluído com sucesso!')
            self.lista_jogadores()
        else:
            self.__tela_jogador.mostra_msg('Jogador não encontrado')

    def buscar_jogador(self):
        id_jogador = TelaJogador.seleciona_jogador(self)
        jogador = self.pega_jogador_por_id(id_jogador)
        
        if (jogador is not None):
            self.__tela_jogador.mostra_jogador({"cod": jogador.id, "nome": jogador.nome, "data de nascimento": jogador.data_nascimento, "pontuação": jogador.pontuacao})
            while True:
                self.__tela_jogador.mostra_msg(f'Partidas de {jogador.nome}:')
                if len(self.__controlador_sistema.controlador_partida.partidas)==0:
                    self.__tela_jogador.mostra_msg(f'{jogador.nome} não tem partidas')
                    break
                else:
                    for partida in self.__controlador_sistema.controlador_partida.partidas:
                        if partida.jogador == jogador:
                            self.__controlador_sistema.tela_partida.mostra_partida({"jogador": partida.jogador, "data/hora": partida.data_hora, "número de rodadas": len(partida.rodadas), "vencedor": partida.vencedor})
                    break
        else:
            self.__tela_jogador.mostra_msg('Jogador não encontrado')
            
    def ranking(self):
        jogs = self.__jogadores
        jogs.sort(key=lambda player: player.pontuacao, reverse=True)

        for player in jogs:
            self.__tela_jogador.ranking(f'{player.nome} Pontuação: {player.pontuacao}')
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_jogador, 2: self.alterar_jogador, 3: self.lista_jogadores, 4: self.excluir_jogador, 5: self.buscar_jogador, 6:self.ranking, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_jogador.tela_opcoes()]()
