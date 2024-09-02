from animal_base import Animal

class Mamifero(Animal):
    def __init__(self, nome, idade, tem_pelo: bool):
        super().__init__(nome, idade)
        self.tem_pelo = tem_pelo

    def fazer_som(self):
        return "O mamífero está rugindo."
    
    def movimentar(self):
        return super().movimentar()