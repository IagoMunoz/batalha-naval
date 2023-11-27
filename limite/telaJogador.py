import random
from datetime import datetime
import PySimpleGUI as sg


class TelaJogador():
    def __init__(self):
        sg.theme('darkpurple1')
        self.__window = None

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

        self.__window = sg.Window('Entrada de Dados').Layout(layout)

        while True:
            event, values = self.__window.read()

            try:
                valor_int = int(values[0])
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError

                self.__window.close()
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

        self.__window = sg.Window('Opções de Jogadores').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Retornar':
                self.__window.close()
                return 0
            elif event == 'Incluir Jogador':
                self.__window.close()
                return 1
            elif event == 'Alterar Jogador':
                self.__window.close()
                return 2
            elif event == 'Listar Jogadores':
                self.__window.close()
                return 3
            elif event == 'Excluir Jogador':
                self.__window.close()
                return 4
            elif event == 'Buscar Jogador':
                self.__window.close()
                return 5
            elif event == 'Ranking de Jogadores':
                self.__window.close()
                return 6

    def pega_dados(self):
        layout = [
            [sg.Text('DADOS JOGADOR', font=('Bookman Old Style', 15))],
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.CalendarButton('Escolher Data', target='date_input', key='-CALENDAR-', format='%d/%m/%Y'),
             sg.InputText(default_text='', size=(20, 1), key='date_input', enable_events=True)],
            [sg.Button('Confirmar', font=('Bookman Old Style', 12))]
        ]

        self.__window = sg.Window('Cadastro de Jogador', layout, finalize=True)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED:
                self.__window.close()
                return None

            elif event == 'Confirmar':
                id = random.randint(0, 1000000)
                nome = values['nome']
                data = values['date_input']  

                try:
                    data_final = datetime.strptime(data, '%d/%m/%Y')
                except ValueError:
                    sg.popup_error('Por favor, selecione uma data válida.')
                    continue

                self.__window.close()
                return {"id": id, "nome": nome, "data de nascimento": data_final}

    
    def mostra_jogador(self, dados_jogador):
        if dados_jogador is None:
            layout = [
                [sg.Text('Sem jogadores cadastrados', font=('Bookman Old Style', 30), justification='center')],
                [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style', 10))]
            ]
            self.__window = sg.Window('Listar jogadores').Layout(layout)

            while True:
                event, values = self.__window.read()

                if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                    self.__window.close()
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
                [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style', 11))]
            ]

            self.__window = sg.Window("Lista de Jogadores", resizable=True).Layout(layout)

            while True:
                event, values = self.__window.read()

                if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                    break

            self.__window.close()

    def mostra_jogador_sozinho(self, id, nome, nascimento, pontuacao):
        layout = [
            [sg.Text("Id: ", font=('Bookman Old Style',15)), sg.Text(id, font=('Bookman Old Style',15))],
            [sg.Text("Nome: ", font=('Bookman Old Style',15)), sg.Text(nome, font=('Bookman Old Style',15))],
            [sg.Text("Data de nascimento: ", font=('Bookman Old Style',15)), sg.Text(str(nascimento), font=('Bookman Old Style',15))],
            [sg.Text("Pontos: ", font=('Bookman Old Style',15)), sg.Text(pontuacao, font=('Bookman Old Style',15))],
            [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style', 12))]
        ]
        self.__window = sg.Window('Listar jogadores').Layout(layout)

        while True:
            event, values = self.__window.Read()

            if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                self.__window.close()
                return None
                
    def mostra_jogador_sozinho_sem_partida(self, id, nome, nascimento, pontuacao, partidas):
        layout = [
            [sg.Text("Id: ", font=('Bookman Old Style', 12)), sg.Text(str(id), font=('Bookman Old Style', 12))],
            [sg.Text("Nome: ", font=('Bookman Old Style', 12)), sg.Text(nome, font=('Bookman Old Style', 12))],
            [sg.Text("Data de nascimento: ", font=('Bookman Old Style', 12)), sg.Text(nascimento, font=('Bookman Old Style', 12))],
            [sg.Text("Pontos: ", font=('Bookman Old Style', 12)), sg.Text(str(pontuacao), font=('Bookman Old Style', 12))],
            [sg.Text("Partidas: ", font=('Bookman Old Style', 12))],
            [sg.Table(values=partidas,
                      headings=["ID", "Data", "Vencedor"],
                      auto_size_columns=False,
                      col_widths=[20, 20, 10],
                      font=('Bookman Old Style', 12),
                      justification='center',
                      key='-TABLE-')],
            [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style', 12))]
        ]

        self.__window = sg.Window('Listar jogadores').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                self.__window.close()
                return None
            
    def sem_jogadores(self):
        layout = [
                [sg.Text('Sem jogadores cadastrados', font=('Bookman Old Style', 15), justification='center')],
                [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style', 10))]
            ]
        self.__window = sg.Window('sem jogadores').Layout(layout)
        
        while True:
                event, values = self.__window.read()

                if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                    self.__window.close()
                    return None
                
    def pop_up(self, mensagem):
        sg.popup(mensagem, font=('Bookman Old Style', 11))
        
    def seleciona_jogador(self, jogadores):
        layout = [
            [sg.Text('Selecione um jogador:', font=('Bookman Old Style', 15))],
            [sg.Combo(jogadores, key='jogador_combo', font=('Bookman Old Style', 12))],
            [sg.Button('Selecionar Jogador', font=('Bookman Old Style', 11)), sg.Button('Cancelar', font=('Bookman Old Style', 11))]
        ]

        self.__window = sg.Window('Seleção de Jogador').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                self.__window.close()
                return None

            elif event == 'Selecionar Jogador':
                jogador_selecionado = values['jogador_combo']
                self.__window.close()
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

        self.__window = sg.Window('Alterar Jogador').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                self.__window.close()
                return None

            elif event == 'Alterar Nome':
                self.__window.close()
                return 1

            elif event == 'Alterar Data de Nascimento':
                self.__window.close()
                return 2

    def alterar_nome(self):
        layout = [
            [sg.Text('Digite o novo nome:', font=('Bookman Old Style', 15))],
            [sg.InputText(key='novo_nome', font=('Bookman Old Style', 12))],
            [sg.Button('Confirmar', font=('Bookman Old Style', 12)), sg.Button('Cancelar', font=('Bookman Old Style', 12))]
        ]

        self.__window = sg.Window('Alterar Nome').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                self.__window.close()
                return None

            elif event == 'Confirmar':
                novo_nome = values['novo_nome']
                self.__window.close()
                return novo_nome

    def alterar_nascimento(self):
        layout = [
            [sg.Text('Digite a nova data de nascimento:', font=('Bookman Old Style', 15))],
            [sg.InputText(key='nova_data', font=('Bookman Old Style', 12))],
            [sg.Text('', size=(30, 1), key='mensagem', font=('Bookman Old Style', 12), text_color='red')],
            [sg.Button('Confirmar', font=('Bookman Old Style', 12)), sg.Button('Cancelar', font=('Bookman Old Style', 12))]
        ]

        self.__window = sg.Window('Alterar Data de Nascimento').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                self.__window.close()
                return None

            elif event == 'Confirmar':
                nova_data = values['nova_data']
                ver = self.verifica_data(nova_data)
            
                if ver:
                    data_final = datetime.strptime(nova_data, '%d/%m/%Y')
                    self.__window.close()
                    return data_final
                else:
                    sg.popup_error('Data inválida! Digite a data no formato "DD/MM/AAAA".')

    def ranking(self, jogadores):
        layout = [
            [sg.Text('Ranking de Jogadores', font=('Bookman Old Style', 15))],
            [sg.Listbox(values=jogadores, size=(30, 10), key='list', enable_events=True, font=('Bookman Old Style', 10))],
            [sg.Button('Voltar', font=('Bookman Old Style', 10))]
        ]
        self.__window = sg.Window('ranking').Layout(layout) 

        while True:
            event, values = self.__window.read()

            if event == sg.WINDOW_CLOSED or event == 'Voltar':
                break
        self.__window.close()
        
    def close(self):
        self.__window.Close()
        
    def open(self):
        button, values = self.__window.Read()
        return button, values