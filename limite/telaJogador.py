import random
from datetime import datetime
import PySimpleGUI as sg


class TelaJogador():
    def __init__(self):
        sg.theme('darkpurple1')

    def verifica_data(self, aux):
        if len(aux)!=10:
            return False

        if (aux[2]!='/' or aux[5]!='/'):
            return False

        if not (aux[0].isdigit() and aux[1].isdigit() and aux[3].isdigit() and aux[4].isdigit() and aux[6].isdigit() and aux[7].isdigit() and aux[8].isdigit() and aux[9].isdigit()):
            return False

        dia, mes, ano = aux.split("/")
        ano = int(ano)
        dia = int(dia)
        mes = int(mes)
        if ano > 1990: #supondo que a empresa iniciou em 1990
            if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes ==12 ):
                if(dia <= 31):
                    return True
            if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
                if(dia <= 30):
                    return True
            if mes == 2:
                if (ano%4== 0 and ano%100!= 0) or (ano%400== 0):
                    if(dia <= 29):
                        return True
                if(dia <= 28):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        layout = [
            [sg.Text(mensagem)],
            [sg.InputText()],
            [sg.Button('OK')]
        ]

        window = sg.Window('Entrada de Dados', layout)

        while True:
            event, values = window.read()

            try:
                valor_int = int(values[0])
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError

                window.close()
                return valor_int

            except ValueError:
                sg.popup_error("Valor incorreto!")
                if ints_validos:
                    sg.popup("Valores válidos: ", ints_validos)

    def tela_opcoes(self):
        layout = [
            [sg.Text('Escolha a opção:', font=("Bookman Old Style", 15))],
            [sg.Button('Incluir Jogador', font=('Bookman Old Style', 12))],
            [sg.Button('Alterar Jogador', font=('Bookman Old Style', 12))],
            [sg.Button('Listar Jogadores', font=('Bookman Old Style', 12))],
            [sg.Button('Excluir Jogador', font=('Bookman Old Style', 12))],
            [sg.Button('Buscar Jogador', font=('Bookman Old Style', 12))],
            [sg.Button('Ranking de Jogadores', font=('Bookman Old Style', 12))],
            [sg.Button('Retornar', font=('Bookman Old Style', 12))]
        ]

        window = sg.Window('Opções de Jogadores', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Retornar':
                window.close()
                return 0
            elif event == 'Incluir Jogador':
                window.close()
                return 1
            elif event == 'Alterar Jogador':
                window.close()
                return 2
            elif event == 'Listar Jogadores':
                window.close()
                return 3
            elif event == 'Excluir Jogador':
                window.close()
                return 4
            elif event == 'Buscar Jogador':
                window.close()
                return 5
            elif event == 'Ranking de Jogadores':
                window.close()
                return 6

    def pega_dados(self):
        layout = [
            [sg.Text('-------- DADOS JOGADOR ----------', font=('Bookman Old Style', 15))],
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Data de nascimento (DD/MM/AAAA):'), sg.InputText(key='data')],
            [sg.Button('Confirmar', font=('Bookman Old Style', 12))]
        ]

        window = sg.Window('Cadastro de Jogador', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                window.close()
                return None

            elif event == 'Confirmar':
                id = random.randint(0, 1000000)
                nome = values['nome']
                data = values['data']

                ver = self.verifica_data(data)

                if ver:
                    data_final = datetime.strptime(data, '%d/%m/%Y')
                    window.close()
                    return {"id": id, "nome": nome, "data de nascimento": data_final}
                else:
                    sg.popup_error('Data inválida! Digite a data no formato "DD/MM/AAAA".')

    
    def mostra_jogador(self, dados_jogador):
        if dados_jogador is None:
            layout = [
                [sg.Text('Sem jogadores cadastrados', font=('Bookman Old Style', 30), justification='center')],
                [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style', 10))]
            ]
            window = sg.Window('Listar jogadores', layout)

            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                    window.close()
                    return None
        else:
            layout = [
                [sg.Table(values=dados_jogador,
                          headings=["ID", "Nome", "Data de Nascimento", "Pontuação"],
                          auto_size_columns=False,
                          col_widths=[20, 20, 20, 10], 
                          font=('Bookman Old Style', 15),
                          justification='center',
                          key='-TABLE-')],
                [sg.Button("Retornar", key="-RETORNAR-")]
            ]

            window = sg.Window("Lista de Jogadores", layout, resizable=True)

            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                    break

            window.close()

    def mostra_jogador_sozinho(self, id, nome, nascimento, pontuacao):
        layout = [
            [sg.Text("Id: ", font=('Bookman Old Style')), sg.Text(id, font=('Bookman Old Style'))],
            [sg.Text("Nome: ", font=('Bookman Old Style')), sg.Text(nome, font=('Bookman Old Style'))],
            [sg.Text("Data de nascimento: ", font=('Bookman Old Style')), sg.Text(str(nascimento), font=('Bookman Old Style'))],
            [sg.Text("Pontos: ", font=('Bookman Old Style')), sg.Text(pontuacao, font=('Bookman Old Style'))],
            [sg.Button("Retornar", key="-RETORNAR-")]
        ]
        window = sg.Window('Listar jogadores', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                window.close()
                return None
                
    def mostra_jogador_sozinho_sem_partida(self, id, nome, nascimento, pontuacao, partidas):
        layout = [
            [sg.Text("Id: ", font=('Bookman Old Style', 12)), sg.Text(str(id), font=('Bookman Old Style', 12))],
            [sg.Text("Nome: ", font=('Bookman Old Style', 12)), sg.Text(nome, font=('Bookman Old Style', 12))],
            [sg.Text("Data de nascimento: ", font=('Bookman Old Style', 12)), sg.Text(str(nascimento), font=('Bookman Old Style', 12))],
            [sg.Text("Pontos: ", font=('Bookman Old Style', 12)), sg.Text(str(pontuacao), font=('Bookman Old Style', 12))],
            [sg.Table(values=partidas,
                      headings=["ID", "Nome", "Data de Nascimento", "Pontuação"],
                      auto_size_columns=False,
                      col_widths=[20, 20, 20, 10],
                      font=('Bookman Old Style', 12),
                      justification='center',
                      key='-TABLE-')],
            [sg.Button("Retornar", key="-RETORNAR-")]
        ]

        window = sg.Window('Listar jogadores', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                window.close()
                return None
        
    def seleciona_jogador(self, jogadores):
        layout = [
            [sg.Text('Selecione um jogador:')],
            [sg.Combo(jogadores, key='jogador_combo')],
            [sg.Button('Selecionar Jogador'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Seleção de Jogador', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Selecionar Jogador':
                jogador_selecionado = values['jogador_combo']
                window.close()
                return jogador_selecionado

    def mostra_msg(self, msg):
        print(msg)

    def mudar_jogador(self):
        layout = [
            [sg.Text('Escolha a opção:', font=('Bookman Old Style', 15))],
            [sg.Button('Alterar Nome', font=('Bookman Old Style', 12))],
            [sg.Button('Alterar Data de Nascimento', font=('Bookman Old Style', 12))],
            [sg.Button('Cancelar', font=('Bookman Old Style', 12))]
        ]

        window = sg.Window('Alterar Jogador', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Alterar Nome':
                window.close()
                return 1

            elif event == 'Alterar Data de Nascimento':
                window.close()
                return 2

    def alterar_nome(self):
        layout = [
            [sg.Text('Digite o novo nome:', font=('Bookman Old Style', 15))],
            [sg.InputText(key='novo_nome', font=('Bookman Old Style', 12))],
            [sg.Button('Confirmar', font=('Bookman Old Style', 12)), sg.Button('Cancelar', font=('Bookman Old Style', 12))]
        ]

        window = sg.Window('Alterar Nome', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Confirmar':
                novo_nome = values['novo_nome']
                window.close()
                return novo_nome

    def alterar_nascimento(self):
        layout = [
            [sg.Text('Digite a nova data de nascimento:', font=('Bookman Old Style', 15))],
            [sg.InputText(key='nova_data', font=('Bookman Old Style', 12))],
            [sg.Text('', size=(30, 1), key='mensagem', font=('Bookman Old Style', 12), text_color='red')],
            [sg.Button('Confirmar', font=('Bookman Old Style', 12)), sg.Button('Cancelar', font=('Bookman Old Style', 12))]
        ]

        window = sg.Window('Alterar Data de Nascimento', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                window.close()
                return None

            elif event == 'Confirmar':
                nova_data = values['nova_data']
                ver = self.verifica_data(nova_data)
            
                if ver:
                    data_final = datetime.strptime(nova_data, '%d/%m/%Y')
                    window.close()
                    return data_final
                else:
                    sg.popup_error('Data inválida! Digite a data no formato "DD/MM/AAAA".')

    def ranking(self, ranking):
        print(ranking)