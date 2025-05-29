class Eleicao:
    def __init__(self, total_eleitores, validos, brancos, nulos):
        self.total = total_eleitores
        self.validos = validos
        self.brancos = brancos
        self.nulos = nulos

    def percentual_validos(self):
        return (self.validos / self.total) * 100

    def percentual_brancos(self):
        return (self.brancos / self.total) * 100

    def percentual_nulos(self):
        return (self.nulos / self.total) * 100
