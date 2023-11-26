

def fimpartida(pontos, winjog):


    if winjog:
        mensagem = "Você venceu!! Parabéns!!"
    else:
        mensagem = "Você perdeu :( Mais sorte na próxima!"

    layout = [
        [sg.Text(mensagem)],
        [sg.Text(f'Sua pontuação foi de: {pontos} pontos')],
        [sg.Button('OK')]
    ]

    window = sg.Window('Resultado', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'OK':
            break

    window.close()


