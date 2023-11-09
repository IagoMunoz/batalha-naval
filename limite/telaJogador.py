import random
from datetime import datetime
class TelaJogador():
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
        if ano>1990: #supondo que a empresa iniciou em 1990
            if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
                if(dia<=31):
                    return True
            if (mes==4 or mes==6 or mes==9 or mes==11):
                if(dia<=30):
                    return True
            if mes==2:
                if (ano%4==0 and ano%100!=0) or (ano%400==0):
                    if(dia<=29):
                        return True
                if(dia<=28):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def tela_opcoes(self):
        print("-------- Jogadores ----------")
        print("Escolha a opcão:")
        print("1 - Incluir Jogador")
        print("2 - Alterar Jogador")
        print("3 - Listar Jogadores")
        print("4 - Excluir Jogador")
        print("5 - Buscar Jogador")
        print('6 - Ranking de Jogadores')
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha a opcão: ", [1,2,3,4,5,6,0])
        return opcao
    
    def pega_dados(self):
        print("-------- DADOS JOGADOR ----------")
        #fazer verificação id
        '''id = random.randint(1,200000)'''
        id=1
        
        nome = input("Nome: ")
        #verificacao data nascimento
        data = input("Data de nascimento: ")
        ver = self.verifica_data(data)
        while ver==False:
            data = input('Data inválida! Digite a data de início da obra no formato "DD/MM/AAAA": ')
            ver = self.verifica_data(data)
        data_final = datetime.strptime(data, '%d/%m/%Y')

        return {"id": id, "nome": nome, "data de nascimento": data_final}
    
    def mostra_jogador(self, dados_jogador):
        print("ID DO JOGADOR: ", dados_jogador["cod"])
        print("NOME DO JOGADOR: ", dados_jogador["nome"])
        print("DATA DE NASCIMENTO DO JOGADOR: ", dados_jogador["data de nascimento"])
        print("PONTUAÇÃO DO JOGADOR: ", dados_jogador["pontuação"])
        print("\n")

    def seleciona_jogador(self):
        try:
            id = int(input("ID do jogador que deseja selecionar: "))
            return id
        except ValueError:
            print('O valor digitado não é inteiro')
    
    def mostra_msg(self, msg):
        print(msg)
        
    def mudar_jogador(self):
        print("Escolha a opcão:")
        print("1 - Alterar Nome")
        print("2 - Alterar Data de nascimento")
        
        opcao = self.le_num_inteiro("Escolha a opcão: ", [1,2])
        return opcao
    
    def alterar_nome(self):
        nome = input('Digite o novo nome: ')
        return nome
        
    def alterar_nascimento(self):
        data = input('Digite a nova data de nascimento: ')
        ver = self.verifica_data(data)
        while ver==False:
            data = input('Data inválida! Digite a data de início da obra no formato "DD/MM/AAAA": ')
            ver = self.verifica_data(data)
        data_final = datetime.strptime(data, '%d/%m/%Y')
        return data_final
        
    def ranking(self, ranking):
        print(ranking)
        
    