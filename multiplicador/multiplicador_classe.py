class Tabuada:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        print(f"Tabuada do {self.numero}:")
        for i in range(1,11):
            print(f"{self.numero} x {i} = {self.numero * i}")