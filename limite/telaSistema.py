import PySimpleGUI as sg

class TelaSistema:
    def __init__(self):
        sg.theme('darkpurple1')

    def le_num_inteiro(self, mensagem=" ", ints_validos=None):
        layout = [
            [sg.Text(mensagem)],
            [sg.InputText()],
            [sg.Button('OK', size=(10, 2))]  # Ajuste o tamanho do botão
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

    def tela_inicial(self):
        layout = [
            [sg.Text('Batalha naval', size=(70, 1), font=('Bookman Old Style', 14), justification='center')],
            [sg.Image(filename="C:/trabalho-dsoo-final/limite/onda.png", pad=(0, 20))],
            [
                sg.Button('Iniciar sistema', font=('Bookman Old Style', 12)),
                sg.Button('Finalizar sistema', font=('Bookman Old Style', 12))
            ]
        ]

        window = sg.Window('Opções', layout, element_justification='c')

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Finalizar sistema':
                window.close()
                return 0
            elif event == 'Iniciar sistema':
                window.close()
                return 1
            
    def tela_opcoes(self):
        layout = [
            [sg.Text('Escolha sua opção:', font=("Bookman Old Style", 15), justification='center')],
            [
                sg.Button('Jogadores', size=(10, 2), font=('Bookman Old Style', 10)), 
                sg.Button('Partidas', size=(10, 2), font=('Bookman Old Style', 10)),
                sg.Button('Finalizar sistema', size=(15, 2), font=('Bookman Old Style', 10))
            ]
        ]

        window = sg.Window('Opções', layout)  

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == 'Finalizar sistema':
                window.close()
                return 0
            elif event == 'Jogadores':
                window.close()
                return 1
            elif event == 'Partidas':
                window.close()
                return 2
            
    def mostra_msg(self, msg):
        print(msg)