from entidade.barco_super import BS

class Fragata(BS):
    def __init__(self):
        super().__init__("Fragata", 3)