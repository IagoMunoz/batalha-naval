from controle.controladorPartida import ControladorPartida
from controle.controlador_barco_super import ControladorBarcoSuper
import random
import PySimpleGUI as sg

class TelaRodada():
    def __init__(self):
        self.__controlador_partida = ControladorPartida(self)
        self.__window = None
        sg.theme('darkpurple1')

    @property
    def controlador_partida(self):
        return self.__controlador_partida
    
    def mostra_rodada(self, dados_rodada):
        layout = [
                [sg.Table(values=dados_rodada,
                        headings=["Jogada jogador", "Jogada computador", "Pontos jogador", "Pontos computador"],
                        auto_size_columns=False,
                        col_widths=[22, 22, 22, 22], 
                        font=('Bookman Old Style', 15),
                        justification='center',
                        key='-TABLE-')],
                [sg.Button("Retornar", key="-RETORNAR-")]
            ]
        self.__window = sg.Window("Lista de rodadas", resizable=True).Layout(layout)
        
        while True:
            event, values = self.__window.read()
            if event == 'Retornar' or event == sg.WIN_CLOSED:
                break
        self.__window.close()
    
    
            
            #############################################################################
                
    def rodada1(self, oceano, barcos, jatiro):
        

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

            # Tamanho da fonte inicial
            font_size = 12

            # Layout inicial da janela com os botões
            layout = create_layout(matrix, font_size, barco)

            # Criação da janela
            window = sg.Window('Matriz como Botões', layout)

            # Loop para interação com a janela
            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED:
                    break
                elif isinstance(event, tuple):
                    row, col = event
                    if matrix[row][col] != '~~':
                        continue  # Se o botão pressionado não for '~~', continue no loop
                    selection = show_confirmation_dialog(row+1, col+1, barco)
                    if selection is not None:
                        break  

            # Fechamento da janela ao sair do loop
            window.close()
            return selection
        
        


        for ycolunas in range(len(oceano)):
            for xlinha in range(len(oceano[ycolunas])):
                tembarco=False
                for barco in barcos:
                    for posicao in barco['_BS__posicoes']:
                        if posicao[0]==ycolunas and posicao[1]==xlinha:
                            if barco['_BS__estado']==True:
                                if posicao[2]==True:
                                    
                                    oceano[ycolunas][xlinha] = '~~'
                                    tembarco=True
                                else:
                                    oceano[ycolunas][xlinha] = '%'
                                    tembarco=True
                            else:
                                oceano[ycolunas][xlinha] = barco['_BS__nome'][0].lower()
                                tembarco=True

                if tembarco == False:
                    marzin=True
                    for jatiroin in jatiro:
                        if jatiroin[0] == ycolunas+1 and jatiroin[1] == xlinha+1:
                            oceano[ycolunas][xlinha] = '@'
                            marzin=False
                    if marzin==True:
                        oceano[ycolunas][xlinha] = '~~'
        
        selection = faztela(oceano, barco)
        
        valory = selection[0]
        valorx = selection[1]

    


        #y é o primeiro  e x o segundo
        return (valory, valorx, True)
        
            
        
        #retorna true se acerta e false se erra
    ###################################################### 
    def tela_acerto(self, oceano, barcos, jatiro, tiro):

        def faztela(mostra):
            if mostra == 'mar':
                sg.popup('Você acertou o mar :(')
            elif mostra == 'barco':
                sg.popup('Você acertou um barco, mas não destruiu ele ainda')
            else:
                sg.popup(f'Parabéns! Você acertou um barco do tipo {mostra} e destruiu ele')

        for ycolunas in range(len(oceano)):
            for xlinha in range(len(oceano[ycolunas])):
                tembarco=False
                for barco in barcos:
                    for posicao in barco['_BS__posicoes']:
                        if posicao[0]==ycolunas and posicao[1]==xlinha:
                            if barco['_BS__estado']==True:
                                if posicao[2]==True:
                                    
                                    oceano[ycolunas][xlinha] = 'barco'
                                    tembarco=True
                                else:
                                    oceano[ycolunas][xlinha] = 'barco'
                                    tembarco=True
                            else:
                                oceano[ycolunas][xlinha] = barco['_BS__nome']
                                tembarco=True

                if tembarco == False:
                    marzin=True
                    for jatiroin in jatiro:
                        if jatiroin[0] == ycolunas+1 and jatiroin[1] == xlinha+1:
                            oceano[ycolunas][xlinha] = 'mar'
                            marzin=False
                    if marzin==True:
                        oceano[ycolunas][xlinha] = 'mar'
        
        prateleira = oceano[tiro[0]-1][tiro[1]-1]

        faztela(prateleira)

        ####################################################################################
    def conc_rodada(self, jogadnv, acertou):
        if jogadnv==True:
            acertou+=1
        return acertou
            
    def rodada1_comp(self, oceano, barcos, jatiro):
        contx=1
        for y in range(len(oceano[0])):
            if y>8:
                print("",y+1,end='')
            else:
                print("",y+1,end=' ')
        print("")

        for ycolunas in range(len(oceano)):
            for xlinha in range(len(oceano[ycolunas])):
                tembarco=False
                for barco in barcos:
                    for posicao in barco['_BS__posicoes']:
                        if posicao[0]==ycolunas and posicao[1]==xlinha:
                            if barco['_BS__estado']==True:
                                if posicao[2]==True:
                                    print ('[~]', end='')
                                    tembarco=True
                                else:
                                    print('[%]',end='')
                                    tembarco=True
                            else:
                                print('[{}]'.format(barco['_BS__nome'][0]).lower(),end='')
                                tembarco=True

                if tembarco == False:
                    marzin=True
                    for jatiro in jatiro:
                        if jatiro[0] == ycolunas+1 and jatiro[1] == xlinha+1:
                            print('[@]',end='')
                            marzin=False
                    if marzin==True:
                        print('[~]',end='')

            if contx==ycolunas:
                print(" ", contx)
            else:
                print("")
            contx+=1


    def escolhexy_rodada_comp(self, oceano, barcos, jatiro):
                
        print("computador irá atirar")
        print("")
        while True:
            aux = 0
            valory = (random.randint(1, (len(oceano))))
            valorx = (random.randint(1, (len(oceano[0]))))
            for tiro in jatiro:
                if tiro[0]==valory or tiro[1]==valorx:
                    valory = (random.randint(1, (len(oceano))))
                    valorx = (random.randint(1, (len(oceano[0]))))
                else:
                    aux +=1
            if aux==len(jatiro):
                break
                            
                    

        contx=1
        for y in range(len(oceano[0])):
            if y+1==valorx:
                print("   ",valorx,end='')
            else:
                print(" ",end=' ')
        print("")

        for ycolunas in range(len(oceano)):
            for xlinha in range(len(oceano[ycolunas])):
                tembarco=False
                for barco in barcos:
                
                    
                    for posicao in ['_BS__posicoes']:
                        if posicao[0]==ycolunas and posicao[1]==xlinha:

                            if valory-1==ycolunas and valorx-1==xlinha:
                                tembarco=True
                                print ('[X]',end='')
                                tembarco=True

                            elif barco['_BS__estado']==True:
                                if posicao[2]==True:
                                    tembarco=True
                                    print ('[~]', end='')
                                    tembarco=True
                                else:
                                    tembarco=True
                                    print('[%]',end='')
                                    tembarco=True
                            else:
                                tembarco=True
                                print('[{}]'.format(barco['_BS__nome'][0]).lower(),end='')
                                tembarco=True
                        

                if tembarco == False:
                    marzin=True
                    for jatiroin in jatiro:
                        if jatiroin[0] == ycolunas+1 and jatiroin[1] == xlinha+1:
                            print('[@]',end='')
                            marzin=False
                    if marzin==True:
                        if valory-1==ycolunas and valorx-1==xlinha:
                            print ('[X]',end='')
                        else:
                            print('[~]',end='')
                        
                    

            if contx==valory:
                print("", contx)
            else:
                print("")
            contx+=1

        return (valory, valorx, True)
                
    def conc_rodada_comp(self, jogadnv, acertou):
        if jogadnv==True:
            
            acertou+=1
            
           
            print('IH ALA O COMPIUTER ACERTOU')
            
        else:
            print('computador errou! :)')

        return acertou
        