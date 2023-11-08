import random
import time
class TelaPartida():
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
        print("-------- Partidas ----------")
        print("Escolha a opcão:")
        print("1 - Nova Partida")
        print("2 - Listar Partidas")
        print("3 - Buscar Partida")
        print("4 - Excluir Partida")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcão: ", [1,2,3,4,0])
        return opcao
    
    def mostra_partida(self, dados_partida):
        print("ID DA PARTIDA: ", dados_partida["id"])
        print("JOGADOR DA PARTIDA: ", dados_partida["jogador"])
        print("DATA DA PARTIDA: ", dados_partida["data/hora"])
        print("NÚMERO DE RODADAS: ", dados_partida["número de rodadas"])
        print("VENCEDOR: ", dados_partida["vencedor"])
        print("\n")
    
    def pega_jogador(self):
        try:
            id = int(input('Digite o ID do jogador da partida: '))
            return id 
        except ValueError:
            print('O valor digitado não é inteiro')
    
    def pega_partida(self):
        try:
            id = int(input('Digite o ID da partida: '))
            return id 
        except ValueError:
            print('O valor digitado não é inteiro')

    def seleciona_jogo(self):
        print('------- SELECIONE O TIPO DE OCEANO -------')
        print()
        print('1) Oceano padrão (10x10)')
        print('2) Oceano personalizado')

        opcao = self.le_num_inteiro('Selecione a opção: ', [1,2])
        if opcao==1:
            return [10,10]
        if opcao==2:
            # while True:
            #     try:
            #         tamanho_y, tamanho_x = int(input('Digite os tamanhos da tela do oceano, coluna e depois linha(ex: 10 10):')).split()
            #         if tamanho_y<6 or tamanho_x<6:
            #             tamanho_y, tamanho_x = int(input('Valores muito pequenos. Digite os valores novamente um ao lado do outro: ')).split()
            #         elif tamanho_y>30 or tamanho_x>30:
            #             tamanho_y, tamanho_x = int(input('Valores muito grandes. Digite os valores novamente um ao lado do outro: ')).split()
            #         else:
            #             break
            #     except ValueError:
            #         print('Os valores digitados não são inteiros')

        #o y é linha e o x coluna
            tamanho_y=int(input("ai que nao sei o que linha: "))
            tamanho_x=int(input("ai que nao sei o que linha: "))
            return [tamanho_y, tamanho_x]

    def adicionar_posicao(self, barco, oceano, barcos):
        
        print('bem vindo ao sistema de posicionamento de barcos')
        print('você vai fazer o posicionamento de um(a) {} agora'.format(barco['_BS__nome']))
        print("  ")

        poretorna=False
        valory=0
        valorx=0
        
        while poretorna==False:

            contx=1
            for y in range(len(oceano[0])):
                if y>8:
                    print("",y+1,end='')
                else:
                    print("",y+1,end=' ')
            print("")

            for ycolunas in range(len(oceano)):
                time.sleep(0.005)
                for xlinhas in range(len(oceano[ycolunas])):
                    time.sleep(0.005)
                    tembarco=False
                    for barcoxy in barcos:
                        for casas in range(len(barcoxy['_BS__posicoes'])):
                            if barcoxy['_BS__posicoes'][casas]==[ycolunas,xlinhas, True]:
                                    if barcoxy['_BS__estado']==True:
                                        print ('[{}]'.format(barcoxy['_BS__nome'][0]),end='')
                                        tembarco=True

                    if tembarco==False:               
                        print ("[~]",end='')

                print("", contx)
                contx+=1

            print("  ")
            while True:
                try:
                    valory,valorx = map(int, input("Digite onde quer botar linha e coluna: ").split())
                
                    if valory>(len(oceano)) or valorx>(len(oceano[1])):
                        valory,valorx = map(int, input("Valores muito altos. Digite novamente onde quer botar linha e coluna: ").split())
                    else:
                        break
                except ValueError:
                    print('Os valores digitados não são inteiros')
                    
            while True:
                for barcoxy in barcos:
                    for posicao in barcoxy['_BS__posicoes']:
                        if posicao[0] == valory-1 and posicao[1] == valorx-1:
                            try:
                                valory, valorx = map(int, input("Posição já colocada. Digite onde quer botar linha e coluna: ").split())
                            except ValueError:
                                print('Os valores digitados não são inteiros')            
                else:
                    break
                                       
            contx=1
            for y in range(len(oceano[0])):
                if y+1==valorx:
                    print("",valorx,end='')
                else:
                    print("  ",end=' ')
            print("")

            for ycolunas in range(len(oceano)):
                time.sleep(0.005)
                for xlinhas in range(len(oceano[ycolunas])):
                    time.sleep(0.005)
                    tembarco=False
                    for barcoxy in barcos:
                        for casas in range(len(barcoxy['_BS__posicoes'])):
                            if barcoxy['_BS__posicoes'][casas]==[ycolunas,xlinhas, True]:
                                    if barcoxy['_BS__estado']==True:
                                        print ('[{}]'.format(barcoxy['_BS__nome'][0]),end='')
                                        tembarco = True
                   
                    if tembarco==False:               
                        if ycolunas==valory-1 and xlinhas==valorx-1:
                            print('[!]',end='')         
                        else:
                            print ("[~]",end='')
                            
                if contx==valory:
                    print ("", valory)
                else:
                    print("")
                contx+=1      
            
            uauaux=input('deseja botar esta posicao? [s/n]: ')
            if uauaux=="s":
                poretorna=True
                
                
        print("  ")
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
        
        
        print('bem vindo a continuaçao sistema de posicionamento de barcos')
        print('você vai continuar o posicionamento de um(a) {} agora'.format(barco['_BS__nome']))
        print("  ")



        
        
        contx=1
        for y in range(len(oceano[0])):
            if y>8:
                print("",y+1,end='')
            else:
                print("",y+1,end=' ')
        print("")
        
        for ycolunas in range(len(oceano)):
            for xlinhas in range(len(oceano[y])):
                tembarco=False
                for barcoxy in barcos:
                    for casas in range(len(barcoxy['_BS__posicoes'])):
                            if barcoxy['_BS__posicoes'][casas]==[ycolunas,xlinhas, True]:
                                if barcoxy['_BS__estado']==True:
                                    print ('[{}]'.format(barcoxy['_BS__nome'][0]),end='')
                                    tembarco=True

                if tembarco==False:               
                    print ("[~]",end='')

            print("", contx)
            contx+=1
        print("")
        print("voce pode estender o barco nas seguintes direçoes:")
        print("")
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

        

        print("")
        if cima==True:
            print (" cima")

        if baixo==True:
            print (" baixo")

        if esquerda==True:
            print (" esquerda")

        if direita==True:
            print (" direita")
        print("")
        auxescolha = input("em qual das posicçoes voce deseja botas: ")
        print(barco['_BS__nome'])

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
    
