import PySimpleGUI as sg

class OceanoGrandeException(Exception):
    def __init__(self, tamanhos):
        self.mensagem = "Tamanho {} maior do que o possível"
        super().__init__(self.mensagem.format(tamanhos))