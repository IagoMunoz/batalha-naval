import PySimpleGUI as sg
import time

# Função para criar a janela com a matriz de botões desabilitados
def show_matrix(matrix):
    layout = []
    for row in matrix:
        row_layout = []
        for col in row:
            button = sg.Button(col, disabled=True, size=(2, 1), pad=(1,1))
            row_layout.append(button)
        layout.append(row_layout)

    window = sg.Window('Matriz de Botões', layout, finalize=True)
    window.read(timeout=3000)  # Mantém a janela aberta por 2 segundos
    window.close()

# Função para exibir o popup com a mensagem
def show_popup(message):
    sg.popup(message)

def show_matrix2(matrix, highlight_coords):
    layout = []
    for i, row in enumerate(matrix):
        row_layout = []
        for j, col in enumerate(row):
            button = sg.Button(col, disabled=True, size=(2, 1), pad = (1,1))
            if [i, j] == highlight_coords:  # Destaca as coordenadas fornecidas
                button = sg.Button(col, disabled=True, size=(2, 1), pad = (1,1), button_color=('white', 'red'))  # Destaca a posição em vermelho
            else:
                button = sg.Button(col, disabled=True, size=(2, 1), pad = (1,1))
            row_layout.append(button)
        layout.append(row_layout)

    window = sg.Window('Matriz de Botões', layout, finalize=True)
    window.read(timeout=2000)  # Mantém a janela aberta por 2 segundos
    window.close()

# Matriz de exemplo (você pode substituir esta matriz por qualquer outra)
matrix = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

# Exibindo a matriz na janela
show_matrix(matrix)

# Lista para passar como mensagem no popup
lista_para_popup = ['item1', 'item2', 'item3']  # Substitua isso pela sua lista

# Exibindo o popup com a mensagem
show_popup(f"O computador vai atirar em {lista_para_popup}")

coordenadas_destaque = [1, 1]

# Exibindo a matriz na janela com posições destacadas
show_matrix2(matrix, coordenadas_destaque)

