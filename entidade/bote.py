from entidade.barco_super import BarcoSuper

class Bote(BarcoSuper):
    def __init__(self):
        super().__init__("Bote", 1)