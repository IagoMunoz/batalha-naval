import random
import time
import PySimpleGUI as sg


class TelaPartida():
    def __init__(self):
        sg.theme('darkpurple1')
        self.__window = None
        
    def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido) #tenta transformar o valor lido em inteiro.
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError #será lançada apenas se o número não é o esperado
                return valor_int
            except ValueError: #aqui cai se não for int ou se não for valido
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)
    
    
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

    
    def mostra_partida(self, dados_partida):
        if dados_partida==None:
            layout = [
                [sg.Text('Sem partidas cadastradas', font=('Bookman Old Style', 15), justification='center')],
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
                    [sg.Table(values=dados_partida,
                            headings=["ID", "Jogador", "Data", "Núm de rodadas", "Vencedor"],
                            auto_size_columns=False,
                            col_widths=[20, 20, 20, 20, 20], 
                            font=('Bookman Old Style', 15),
                            justification='center',
                            key='-TABLE-')],
                    [sg.Button("Retornar", key="-RETORNAR-")]
                ]
            self.__window = sg.Window("Lista de partidas", resizable=True).Layout(layout)
            
            while True:
                event, values = self.__window.read()
                if event == 'Retornar' or event == sg.WIN_CLOSED:
                    break
                self.__window.close()
            
    def pega_jogador(self):
        try:
            id = int(input('Digite o ID do jogador da partida: '))
            return id 
        except ValueError:
            print('O valor digitado não é inteiro')
    
    def pega_partida(self, partidas):
        layout = [
            [sg.Text('Selecione uma partida:')],
            [sg.Combo(partidas, key='partida_combo')],
            [sg.Button('Selecionar partida'), sg.Button('Cancelar')]
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
                return [5,5]
            else:
                layout = [
                    [sg.Text('Tamanho x:'), sg.InputText(key='x')],
                    [sg.Text('Tamanho y:'), sg.InputText(key='y')],
                    [sg.Button('Enviar', font=('Bookman Old Style', 12))]
                ]
                self.__window = sg.Window('Tamanho oceano').Layout(layout)
                
                
                while True:
                    event, values = self.__window.read()
                    if event == sg.WIN_CLOSED :
                        self.__window.close()
                        
                    elif event == 'Enviar':
                        x = int(values['x'])
                        y = int(values['y'])
                        if x > 21 or y > 48:
                            sg.popup_error('Tamanho maior do que o possível')
                        else:
                            self.__window.close()
                            return [x, y]
                        
                    elif event == 'Enviar':
                        x = values[x]
                        y = values[y]
                        self.__window.close()
                        return[x,y]
                
        '''opcao = self.le_num_inteiro('Selecione a opção: ', [1,2])
        if opcao==1:
            return [10,10]
        if opcao==2:
           
        #o y é linha e o x coluna
        #pra apresentaçao os limites sao 21 e 48
        #pra os nossos notebooks, por uma questao de teste, sao tipo 11 e 24
            tamanho_y=int(input("ai que nao sei o que linha: "))
            tamanho_x=int(input("ai que nao sei o que coluna "))
            return [tamanho_y, tamanho_x]'''
    def mostrar_ordem_posicionamento(self):
        layout = [
            [sg.Text('Você irá posicionar seus barcos na seguinte ordem:')],
            [sg.Text('Quatro Botes')],
            [sg.Text('Três Submarinos')],
            [sg.Text('Três Fragatas')],
            [sg.Text('Um porta-aviões')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Posicionamento de Barcos', layout)

        while True:
            event, _ = window.read()

            if event == sg.WINDOW_CLOSED or event == 'OK':
                break

        window.close()


    def adicionar_posicao(self, barco, oceano, barcos):

        def faztela( matrix, barco):

            def create_layout(matrix, font_size, barco):
                layout = [
                    [sg.Text(f'Escolha a posição para seu/sua {barco["_BS__nome"]}', font=('Helvetica', 14))],  # Texto acima do layout principal
                ]
                for i, row in enumerate(matrix):
                    row_layout = []
                    for j, value in enumerate(row):
                        if value != '~~':  # Verifica se o valor do botão não é '~~'
                            button = sg.Button(str(value), size=(2, 1), key=(i, j), font=('Helvetica', font_size), pad=(1, 1), disabled=True, button_color=('white', 'white'))
                        else:
                            button = sg.Button(str(value), size=(2, 1), key=(i, j), font=('Helvetica', font_size), pad=(1, 1))
                        row_layout.append(button)
                    layout.append(row_layout)
                return layout

            # Função para mostrar a caixa de diálogo de confirmação
            def show_confirmation_dialog(row, col, barco):
                layout = [
                    [sg.Text(f'Deseja posicionar o/a {barco["_BS__nome"]} na linha: {row} e coluna: {col}?')],
                    [sg.Button('Sim'), sg.Button('Cancelar')]
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
                                    '''print ('[{}]'.format(barcoxy['_BS__nome'][0]),end='')'''
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


            print("  ")
            valory,valorx = map(int, (random.randint(1, len(oceano)),(random.randint(1, len(oceano[0])))))
            while True:
                for barcoxy in barcos:
                    for coor in barcoxy['_BS__posicoes']:
                        
                        if coor[0]==valory-1 and coor[1]==valorx-1:
                            valory,valorx = map(int, (random.randint(1, len(oceano)),(random.randint(1, len(oceano[0])))))
                else:
                    break
            poretorna=True
                
                
        print("  ")
        return [valory-1,valorx-1]
    
    def continuar_posicao(self, barco, oceano, barcos, posicao):


        def faztela(matrix, barco, posicao, lista_bool_pos ):
            def create_layout(matrix, font_size, barco, highlighted_position=None, directions_visibility=None):
                layout = [
                    [sg.Text(f'Escolha uma posição inicial para o/a {barco["_BS__nome"]}', font=('Helvetica', 14))],  # Texto acima do layout principal
                ]
                for i, row in enumerate(matrix):
                    row_layout = []
                    for j, cell in enumerate(row):
                        button_color = ('black', 'yellow') if [i, j] == highlighted_position else ('black', 'white')
                        button = sg.Button(str(cell), size=(2, 1), disabled=True, font=('Helvetica', font_size),
                                        button_color=button_color, pad=(2, 1))
                        row_layout.append(button)
                    layout.append(row_layout)

                # Adicionando texto para posicionar o barco
                layout.append([sg.Text(f'Você deseja estender o/a {barco["_BS__nome"]} em que direção?')])

                # Adicionando botões de direção de acordo com a visibilidade
                if directions_visibility:
                    direction_buttons = []
                    if directions_visibility.get('Cima', False):
                        direction_buttons.append(sg.Button('Cima'))
                    if directions_visibility.get('Baixo', False):
                        direction_buttons.append(sg.Button('Baixo'))
                    if directions_visibility.get('Esquerda', False):
                        direction_buttons.append(sg.Button('Esquerda'))
                    if directions_visibility.get('Direita', False):
                        direction_buttons.append(sg.Button('Direita'))

                    layout.append(direction_buttons)

                return layout

            # Função para criar layout da janela de confirmação da direção
            def create_confirmation_layout(direction):
                layout = [
                    [sg.Text(f'Deseja estender na direção: {direction}?')],
                    [sg.Button('Cancelar'), sg.Button('Confirmar')]
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
                                    '''print ('[{}]'.format(barcoxy['_BS__nome'][0]),end='')'''
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

        print("")
        if cima==True:
            lista_bool_pos.append(True)
        else:
            lista_bool_pos.append(False)

        if baixo==True:
            lista_bool_pos.append(True)
        else:
            lista_bool_pos.append(False)
        if esquerda==True:
            lista_bool_pos.append(True)
        else:
            lista_bool_pos.append(False)
        if direita==True:
            lista_bool_pos.append(True)
        else:
            lista_bool_pos.append(False)

        
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
        
        auxrandom = random.randint(0,len(socorromeudeus)-1)
        auxescolha = socorromeudeus[auxrandom]
        
        return auxescolha
    def mostra_msg(self, msg):
        print(msg)
    
