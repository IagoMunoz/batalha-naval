import random
import time
import PySimpleGUI as sg
import pygame as pygame
from exception.oceano_pequeno_exception import OceanoPequenoException
from exception.oceano_grande_exception import OceanoGrandeException

class TelaPartida():
    def __init__(self):
        sg.theme('darkpurple1')
        self.__window = None
        
    def pop_up(self, mensagem):
        sg.popup(mensagem, font=('Bookman Old Style', 11))
        
    def play_sound(self, file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido) 
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError 
                return valor_int
            except ValueError: 
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)

    def mostrar_ordem_posicionamento(self):
        layout = [
            [sg.Text('Você irá posicionar seus barcos na seguinte ordem:', font=('Bookman Old Style', 11))],
            [sg.Text('Quatro Botes', font=('Bookman Old Style', 11))],
            [sg.Text('Três Submarinos', font=('Bookman Old Style', 11))],
            [sg.Text('Três Fragatas', font=('Bookman Old Style', 11))],
            [sg.Text('Um porta-aviões', font=('Bookman Old Style', 11))],
            [sg.Button('OK', font=('Bookman Old Style', 11))]
        ]

        window = sg.Window('Posicionamento de Barcos', layout)

        while True:
            event, _ = window.read()

            if event == sg.WINDOW_CLOSED or event == 'OK':
                break

        window.close()
    
    
    def tela_opcoes(self):
        layout = [
            [sg.Text('Escolha a opção:', font=("Bookman Old Style", 15))],
            [sg.Button('Nova Partida', font=('Bookman Old Style', 12))],
            [sg.Button('Listar Partidas', font=('Bookman Old Style', 12))],
            [sg.Button('Buscar Partida', font=('Bookman Old Style', 12))],
            [sg.Button('Excluir Partida', font=('Bookman Old Style', 12))],
            [sg.Button('Retornar', font=('Bookman Old Style', 12))]
        ]

        self.__window = sg.Window('Partidas').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Retornar':
                self.__window.close()
                return 0
            elif event == 'Nova Partida':
                self.__window.close()
                return 1
            elif event == 'Listar Partidas':
                self.__window.close()
                return 2
            elif event == 'Buscar Partida':
                self.__window.close()
                return 3
            elif event == 'Excluir Partida':
                self.__window.close()
                return 4

    
    def sem_partidas(self):
        layout = [
                [sg.Text('Sem partidas cadastradas', font=('Bookman Old Style', 15), justification='center')],
                [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style', 10))]
            ]
        self.__window = sg.Window('sem partidas').Layout(layout)
        
        while True:
                event, values = self.__window.read()

                if event == sg.WIN_CLOSED or event == "-RETORNAR-":
                    self.__window.close()
                    return None
        
    
    def mostra_partidas(self, dados_partida):
        layout = [
                [sg.Table(values=dados_partida,
                        headings=["ID", "Jogador", "Data", "Núm de rodadas", "Vencedor"],
                        auto_size_columns=False,
                        col_widths=[20, 20, 20, 20, 20], 
                        font=('Bookman Old Style', 15),
                        justification='center',
                        key='-TABLE-')],
                [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style', 15))]
            ]
        self.__window = sg.Window("Lista de partidas", resizable=True).Layout(layout)
        
        while True:
            event, values = self.__window.read()
            if event == '-RETORNAR-' or event == sg.WIN_CLOSED:
                break
        self.__window.close()
            
    def mostra_partida_sozinha(self, id, jogador, data, num_rodadas, vencedor, rodadas):
        layout = [
            [sg.Text("Id: ", font=('Bookman Old Style',15)), sg.Text(id, font=('Bookman Old Style',15))],
            [sg.Text("Jogador: ", font=('Bookman Old Style',15)), sg.Text(jogador, font=('Bookman Old Style',15))],
            [sg.Text("Data/hora: ", font=('Bookman Old Style',15)), sg.Text(str(data), font=('Bookman Old Style',15))],
            [sg.Text("Número de rodadas: ", font=('Bookman Old Style',15)), sg.Text(num_rodadas, font=('Bookman Old Style',15))],
            [sg.Text("Vencedor: ", font=('Bookman Old Style',15)), sg.Text(vencedor, font=('Bookman Old Style',15))],
            [sg.Button("Retornar", key="-RETORNAR-", font=('Bookman Old Style',11)), sg.Button("Ver rodadas", key="-RODADAS-", font=('Bookman Old Style',11)) ]
        ]
        self.__window = sg.Window('partida').Layout(layout)
        
        while True:
            event, values = self.__window.read()
            if event == '-RETORNAR-' or event == sg.WIN_CLOSED:
                break
            if event == '-RODADAS-':
                self.__window.close()
                return 0
        self.__window.close()
            
    
    def pega_partida(self, partidas):
        layout = [
            [sg.Text('Selecione uma partida:', font=('Bookman Old Style', 12))],
            [sg.Combo(partidas, key='partida_combo')],
            [sg.Button('Selecionar partida', font=('Bookman Old Style', 11)), sg.Button('Cancelar', font=('Bookman Old Style', 11))]
        ]

        self.__window = sg.Window('Seleção de partida').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Cancelar':
                self.__window.close()
                return None

            elif event == 'Selecionar partida':
                partida_selecionada = values['partida_combo']
                self.__window.close()
                return partida_selecionada

    def seleciona_jogo(self):
        layout = [
            [sg.Text('Selecione o tipo de oceano:', font=("Bookman Old Style", 15))],
            [sg.Button('Oceano padrão', font=('Bookman Old Style', 12))],
            [sg.Button('Oceano personalizado', font=('Bookman Old Style', 12))],
            [sg.Button('Retornar', font=('Bookman Old Style', 12))]
        ]
        
        self.__window = sg.Window('Opções de Jogadores').Layout(layout)

        while True:
            event, values = self.__window.read()

            if event == sg.WIN_CLOSED or event == 'Retornar':
                self.__window.close()
                break
            if event == 'Oceano padrão':
                self.__window.close()
                return [10,10]
            else:
                self.__window.close()
                layout = [
                    [sg.Text('Tamanho x:', font=('Bookman Old Style', 11)), sg.InputText(key='x')],
                    [sg.Text('Tamanho y:', font=('Bookman Old Style', 11)), sg.InputText(key='y')],
                    [sg.Button('Enviar', font=('Bookman Old Style', 12)), sg.Button('Retornar', font=('Bookman Old Style', 12))]
                ]
                self.__window = sg.Window('Tamanho oceano').Layout(layout)
                
                
                while True:
                    event, values = self.__window.read()
                    if event == sg.WIN_CLOSED or event == 'Retornar':
                        self.__window.close()
                        return None
                        
                    elif event == 'Enviar':
                        try:
                            x = int(values['x'])
                            y = int(values['y'])
                            if x<10 or y<10:
                                raise OceanoPequenoException([x, y])
                            elif x>30 or y>30:
                                raise OceanoGrandeException([x, y])
                            else:
                                self.__window.close()
                                return [x, y]
                        except OceanoPequenoException as e:
                            sg.popup_error(e, font=('Bookman Old Style', 11))
                        except OceanoGrandeException as e:
                            sg.popup_error(e, font=('Bookman Old Style', 11))
                        except ValueError:
                            sg.popup_error('Valor inválido! Os valores devem ser número inteiros', font=('Bookman Old Style', 11))
                    elif event == 'Enviar':
                        x = values[x]
                        y = values[y]
                        self.__window.close()
                        return[x,y]
                
    def adicionar_posicao(self, barco, oceano, barcos):
        sg.theme('darkpurple1')

        def faztela( matrix, barco):
            sg.theme('darkpurple1')

            def create_layout(matrix, font_size, barco):
                sg.theme('darkpurple1')
                layout = [
                    [sg.Text(f'Escolha a posição para o/a proximo/a {barco["_BS__nome"]}', font=('Bookman Old Style', 14))],  
                ]
                for i, row in enumerate(matrix):
                    row_layout = []
                    for j, value in enumerate(row):
                        if value != '~~':  
                            button = sg.Button(str(value), size=(2, 1), key=(i, j), font=('Bookman Old Style', 12), pad=(1, 1), disabled=sg.BUTTON_DISABLED_MEANS_IGNORE)
                        else:
                            button = sg.Button(str(value), size=(2, 1), key=(i, j), font=('Bookman Old Style', 12), pad=(1, 1))
                        row_layout.append(button)
                    layout.append(row_layout)
                return layout

            def show_confirmation_dialog(row, col, barco):
                layout = [
                    [sg.Text(f'Deseja posicionar o/a {barco["_BS__nome"]} na linha: {row} e coluna: {col}?' , font=('Bookman Old Style', 12))],
                    [sg.Button('Sim', font=('Bookman Old Style', 12)), sg.Button('Cancelar', font=('Bookman Old Style', 12))]
                ]
                window = sg.Window('Confirmação', layout, finalize=True)
                while True:
                    event, _ = window.read()
                    if event in (sg.WIN_CLOSED, 'Cancelar'):
                        window.close()
                        return None
                    elif event == 'Sim':
                        window.close()
                        return [row, col]

            font_size = 12

            layout = create_layout(matrix, font_size, barco)

            window = sg.Window('Matriz como Botões', layout)

            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED:
                    break
                elif isinstance(event, tuple):
                    row, col = event
                    selection = show_confirmation_dialog(row+1, col+1, barco)
                    if selection is not None:
                        break  
            window.close()
            return selection

        valory=0
        valorx=0

        for ycolunas in range(len(oceano)):
            
            for xlinhas in range(len(oceano[ycolunas])):
                
                tembarco=False
                for barcoxy in barcos:
                    for casas in range(len(barcoxy['_BS__posicoes'])):
                        if barcoxy['_BS__posicoes'][casas]==[ycolunas,xlinhas, True]:
                                if barcoxy['_BS__estado']==True:
                                    oceano[ycolunas][xlinhas] = barcoxy['_BS__nome'][0]
                                    tembarco=True

                if tembarco==False:
                    oceano[ycolunas][xlinhas] = '~~'
        selecao = faztela(oceano, barco)
        
        valory = selecao[0]
        valorx = selecao[1]
       
        return [valory-1,valorx-1]
    
    def adicionar_posicao_comp(self, barco, oceano, barcos):

        poretorna=False
        valory=0
        valorx=0
        
        while poretorna==False:


   
            valory,valorx = map(int, (random.randint(1, len(oceano)),(random.randint(1, len(oceano[0])))))
            while True:
                for barcoxy in barcos:
                    for coor in barcoxy['_BS__posicoes']:
                        
                        if coor[0]==valory-1 and coor[1]==valorx-1:
                            valory,valorx = map(int, (random.randint(1, len(oceano)),(random.randint(1, len(oceano[0])))))
                else:
                    break
            poretorna=True
                
                
    
        return [valory-1,valorx-1]
    
    def continuar_posicao(self, barco, oceano, barcos, posicao):
        sg.theme('darkpurple1')


        def faztela(matrix, barco, posicao, lista_bool_pos ):
            sg.theme('darkpurple1')
            def create_layout(matrix, font_size, barco, highlighted_position=None, directions_visibility=None):
                sg.theme('darkpurple1')
                layout = [
                    [sg.Text(f'Escolha uma posição inicial para o/a {barco["_BS__nome"]}', font=('Bookman Old Style', 14))], 
                ]
                for i, row in enumerate(matrix):
                    row_layout = []
                    for j, cell in enumerate(row):

                        if [i, j] == highlighted_position:
                            button = sg.Button(str(cell), size=(2, 1), disabled=sg.BUTTON_DISABLED_MEANS_IGNORE, font=('Bookman Old Style', 12), button_color=('black', 'yellow'), pad=(2, 1))
                        else: 

                        
                            button = sg.Button(str(cell), size=(2, 1), disabled=sg.BUTTON_DISABLED_MEANS_IGNORE, font=('Bookman Old Style', 12), pad=(2, 1))
                        row_layout.append(button)
                    layout.append(row_layout)

                # Adicionando texto para posicionar o barco
                layout.append([sg.Text(f'Você deseja estender o/a {barco["_BS__nome"]} em que direção?', font=('Bookman Old Style', 12))])

                # Adicionando botões de direção de acordo com a visibilidade
                if directions_visibility:
                    direction_buttons = []
                    if directions_visibility.get('Cima', False):
                        direction_buttons.append(sg.Button('Cima', font=('Bookman Old Style', 10)))
                    if directions_visibility.get('Baixo', False):
                        direction_buttons.append(sg.Button('Baixo', font=('Bookman Old Style', 10)))
                    if directions_visibility.get('Esquerda', False):
                        direction_buttons.append(sg.Button('Esquerda', font=('Bookman Old Style', 10)))
                    if directions_visibility.get('Direita', False):
                        direction_buttons.append(sg.Button('Direita', font=('Bookman Old Style', 10)))

                    layout.append(direction_buttons)
                return layout
            # Função para criar layout da janela de confirmação da direção
            def create_confirmation_layout(direction):
                layout = [
                    [sg.Text(f'Deseja estender na direção: {direction}?', font=('Bookman Old Style', 12))],
                    [sg.Button('Cancelar', font=('Bookman Old Style', 10)), sg.Button('Confirmar', font=('Bookman Old Style', 10))]
                ]
                return layout

            # Tamanho da fonte inicial
            font_size = 12
            # Posição a ser destacada (exemplo: linha 1, coluna 2)
            highlighted_position = posicao
            # Dicionário com a visibilidade dos botões de direção
            directions_visibility = {'Cima': lista_bool_pos[0], 'Baixo': lista_bool_pos[1], 'Esquerda': lista_bool_pos[2], 'Direita': lista_bool_pos[3]}

            # Layout inicial da janela com destaque no botão da posição específica
            layout = create_layout(matrix, font_size, barco, highlighted_position, directions_visibility)

            # Criação da janela
            window = sg.Window('Posicionar Barco', layout)

            # Loop para interação com a janela
            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED:
                    break
                elif event in ('Cima', 'Baixo', 'Esquerda', 'Direita'):
                    selected_direction = event

                    # Criando a janela de confirmação da direção
                    confirmation_layout = create_confirmation_layout(selected_direction)
                    confirmation_window = sg.Window('Confirmação da Direção', confirmation_layout)

                    while True:
                        confirmation_event, _ = confirmation_window.read()

                        if confirmation_event == sg.WIN_CLOSED or confirmation_event == 'Cancelar':
                            break
                        elif confirmation_event == 'Confirmar':
                            break

                    confirmation_window.close()
                    break
            # Fechamento da janela ao sair do loop
            window.close()
            return selected_direction

        for ycolunas in range(len(oceano)):
            for xlinhas in range(len(oceano[ycolunas])):
                tembarco=False
                for barcoxy in barcos:
                    for casas in range(len(barcoxy['_BS__posicoes'])):
                        if barcoxy['_BS__posicoes'][casas]==[ycolunas,xlinhas, True]:
                                if barcoxy['_BS__estado']==True:
                                    oceano[ycolunas][xlinhas] = barcoxy['_BS__nome'][0]
                           
                                    tembarco=True
                if tembarco==False:
                    oceano[ycolunas][xlinhas] = '~~'

        cima=True
        baixo=True
        direita=True
        esquerda=True
       
        bs_tamanho = barco['_BS__tamanho']

        if (posicao[0] - bs_tamanho)+1 < 0:
            cima=False

        for casas in range (bs_tamanho):
            for barcoxy in barcos:
                if barcoxy!=barco:
                    for coor in barcoxy['_BS__posicoes']:
                        if coor[1]==posicao[1] and coor[0]==posicao[0]-casas:
                            cima=False

        if (posicao[0] + bs_tamanho) > len(oceano[1]):
            baixo=False

        for casas in range (bs_tamanho):
            for barcoxy in barcos:
                if barcoxy!=barco:    
                    for coor in barcoxy['_BS__posicoes']:
                        if coor[1]==posicao[1] and coor[0]==posicao[0]+casas:
                            baixo=False

        if (posicao[1] - bs_tamanho)+1 < 0:
            esquerda=False

        for casas in range (bs_tamanho):
            for barcoxy in barcos:
                if barcoxy!=barco:
                    for coor in barcoxy['_BS__posicoes']:
                        if coor[0]==posicao[0] and coor[1]==posicao[1]-casas:
                            esquerda=False

        if (posicao[1] + bs_tamanho) > len(oceano[0]):
            direita=False

        for casas in range (bs_tamanho):
            for barcoxy in barcos:
                if barcoxy!=barco:
                    for coor in barcoxy['_BS__posicoes']:
                        if coor[0]==posicao[0] and coor[1]==posicao[1]+casas:
                            direita=False
        lista_bool_pos=[]
      
        meajuda = 0
        if cima==True:
            lista_bool_pos.append(True)
        else:
            lista_bool_pos.append(False)
            meajuda +=1
            
        if baixo==True:
            lista_bool_pos.append(True)
        else:
            lista_bool_pos.append(False)
            meajuda+=1

        if esquerda==True:
            lista_bool_pos.append(True)
           
        else:
            lista_bool_pos.append(False)
            meajuda +=1

        if direita==True:
            lista_bool_pos.append(True)
         
        else:
            lista_bool_pos.append(False)
            meajuda +=1

        if meajuda ==4:
            return True

        auxescolha = faztela(oceano, barco, posicao, lista_bool_pos)

        return auxescolha

    def continuar_posicao_comp(self, barco, oceano, barcos, posicao):
        
        cima=True
        baixo=True
        direita=True
        esquerda=True

        bs_tamanho = barco['_BS__tamanho']
       
        if (posicao[0] - bs_tamanho)+1 < 0:
            cima=False
        
        for casas in range (bs_tamanho):
            for barcoxy in barcos:
                if barcoxy!=barco:
                    for coor in barcoxy['_BS__posicoes']:
                        if coor[1]==posicao[1] and coor[0]==posicao[0]-casas:
                            cima=False

        if (posicao[0] + bs_tamanho) > len(oceano[0]):
            baixo=False

        for casas in range (bs_tamanho):
            for barcoxy in barcos:
                if barcoxy!=barco:    
                    for coor in barcoxy['_BS__posicoes']:
                        if coor[1]==posicao[1] and coor[0]==posicao[0]+casas:
                            baixo=False

        if (posicao[1] - bs_tamanho)+1 < 0:
            esquerda=False

        for casas in range (bs_tamanho):
            for barcoxy in barcos:
                if barcoxy!=barco:
                    for coor in barcoxy['_BS__posicoes']:
                        if coor[0]==posicao[0] and coor[1]==posicao[1]-casas:
                            esquerda=False

        if (posicao[1] + bs_tamanho) > len(oceano[0]):
            direita=False

       
        for casas in range (bs_tamanho):
            for barcoxy in barcos:
                if barcoxy!=barco:
                    for coor in barcoxy['_BS__posicoes']:
                        if coor[0]==posicao[0] and coor[1]==posicao[1]+casas:
                            direita=False

        socorromeudeus = list()

        
        if cima==True:
            socorromeudeus.append("cima")

        if baixo==True:
            socorromeudeus.append("baixo")

        if esquerda==True:
            socorromeudeus.append("esquerda")

        if direita==True:
            socorromeudeus.append("direita")
        
        if len(socorromeudeus) == 0:
            return True
        else: 
            auxrandom = random.randint(0,len(socorromeudeus)-1)
            auxescolha = socorromeudeus[auxrandom]
            
            return auxescolha

    def fimpartida(self, winjog):
        sg.theme('darkpurple1')

        if winjog:
            mensagem = "Você venceu!! Parabéns!!"
            sound_file_path = 'C:/trabalho-dsoo-final/limite/venceu.mp3'  
            self.play_sound(sound_file_path)
        else:
            mensagem = "Você perdeu :( Mais sorte na próxima!"
            sound_file_path = 'C:/trabalho-dsoo-final/limite/perdeu.mp3'  
            self.play_sound(sound_file_path)

        layout = [
            [sg.Text(mensagem, font=('Bookman Old Style', 11))],
            [sg.Button('OK')]
        ]

        window = sg.Window('Resultado', layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'OK':
                break

        window.close()
    
    def compos(self):
        layout = [
            [sg.Text('Os barcos do computador também foram posicionados.', font=('Bookman Old Style', 11))],
            [sg.Text('Lembre-se: Os oceanos de vocês são diferentes então ele pode ter ', font=('Bookman Old Style', 11))],
            [sg.Text('posicionado tanto nos mesmos lugares quanto em lugares diferentes do seus.', font=('Bookman Old Style', 11))],
            [sg.Text('Quanto a batalha:', font=('Bookman Old Style', 12))],
            [sg.Text('@ siginifica um lugar do oceano que foi acertado, % siginica um bar barco que foi acertado mas nao destruido.', font=('Bookman Old Style', 11))],
            [sg.Text('Barcos ao serem destruidos sao revelados e suas inciais aparecerão em letra minuscula.', font=('Bookman Old Style', 11))],
            [sg.Text('Você poderá ver seus barcos em tempo real enquanto o computador atira neles.', font=('Bookman Old Style', 11))],

            [sg.Button('Entendi', font=('Bookman Old Style', 11))]
        ]

      
        window = sg.Window('Aviso', layout, finalize=True)

       
        while True:
            event, values = window.read()

         
            if event == sg.WINDOW_CLOSED or event == 'Entendi':
                break

   
        window.close()
    
    def repos(self):
        layout = [
            [sg.Text('Você selecionou uma posição inválida', font=('Bookman Old Style', 11))],
            [sg.Text('Por favor, selecione novamente', font=('Bookman Old Style', 11))],
            [sg.Button('OK', font=('Bookman Old Style', 11))]
        ]

        window = sg.Window('Mensagem de Erro', layout, finalize=True)

        while True:
            event, _ = window.read()
            if event == sg.WINDOW_CLOSED or event == 'OK':
                break

        window.close()

    def mostra_msg(self, msg):
        print(msg)
    
