import PySimpleGUI as sg

# Matriz de exemplo
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Função para criar um layout a partir da matriz com botões de tamanho de fonte ajustável
def create_layout(matrix, font_size):
    layout = [
        [sg.Text('Hora de Posicionar', font=('Helvetica', 14))],  # Texto acima do layout principal
    ]
    for i, row in enumerate(matrix):
        row_layout = []
        for j, value in enumerate(row):
            button = sg.Button(str(value), size=(4, 2), key=(i, j), font=('Helvetica', font_size), pad=(2, 2))
            row_layout.append(button)
        layout.append(row_layout)
    return layout

# Função para mostrar a caixa de diálogo de confirmação
def show_confirmation_dialog(row, col):
    layout = [
        [sg.Text(f'Deseja selecionar a posição ({row}, {col})?')],
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

# Tamanho da fonte inicial
font_size = 12

# Layout inicial da janela com os botões
layout = create_layout(matrix, font_size)

# Criação da janela
window = sg.Window('Matriz como Botões', layout)

# Loop para interação com a janela
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif isinstance(event, tuple):
        row, col = event
        selection = show_confirmation_dialog(row, col)
        if selection is not None:
            sg.popup(f'Posição selecionada: {selection}')

    # Verifica se o evento é para aumentar o tamanho da fonte
    if event == '+Fonte':
        font_size += 2
        layout = create_layout(matrix, font_size)
        window.close()
        window = sg.Window('Matriz como Botões', layout)

# Fechamento da janela ao sair do loop
window.close()
