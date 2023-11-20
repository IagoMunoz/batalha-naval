import PySimpleGUI as sg

# Matriz de exemplo
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Função para criar um layout a partir da matriz com destaque em um botão específico
def create_layout(matrix, font_size, highlighted_position=None, directions_visibility=None):
    layout = [
        [sg.Text('Hora de Posicionar', font=('Helvetica', 14))],  # Texto acima do layout principal
    ]
    for i, row in enumerate(matrix):
        row_layout = []
        for j, cell in enumerate(row):
            button_color = ('black', 'yellow') if [i, j] == highlighted_position else ('black', 'white')
            button = sg.Button(str(cell), size=(4, 2), disabled=True, font=('Helvetica', font_size),
                               button_color=button_color, pad=(2, 2))
            row_layout.append(button)
        layout.append(row_layout)

    # Adicionando texto para posicionar o barco
    layout.append([sg.Text('Você deseja posicionar o barco em que direção?')])

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
        [sg.Text(f'Deseja posicionar na direção: {direction}?')],
        [sg.Button('Cancelar'), sg.Button('Confirmar')]
    ]
    return layout

# Tamanho da fonte inicial
font_size = 12
# Posição a ser destacada (exemplo: linha 1, coluna 2)
highlighted_position = [1, 2]
# Dicionário com a visibilidade dos botões de direção
directions_visibility = {'Cima': True, 'Baixo': False, 'Esquerda': True, 'Direita': False}

# Layout inicial da janela com destaque no botão da posição específica
layout = create_layout(matrix, font_size, highlighted_position, directions_visibility)

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
                print(f'Direção selecionada: {selected_direction}')
                break

        confirmation_window.close()

# Fechamento da janela ao sair do loop
window.close()
