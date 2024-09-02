from animal_base import Animal

class Ave(Animal):
    def __init__(self, nome, idade, pode_voar:bool):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def fazer_som(self):
        return super().fazer_som()        

    def movimentar(self):
        if self.pode_voar == True:
            return "O passaro está voando."
        return "O pássaro está caminhando."