from entidade.barco_super import BarcoSuper

class Fragata(BarcoSuper):
    def __init__(self):
        super().__init__("Fragata", 3)