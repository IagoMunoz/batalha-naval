import PySimpleGUI as sg

class OceanoPequenoException(Exception):
    def __init__(self, tamanhos):
        self.mensagem = "Tamanho {} menor do que o possível"
        super().__init__(self.mensagem.format(tamanhos))