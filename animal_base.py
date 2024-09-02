from abc import abstractmethod, ABC

##Classe vai ser abstrata
class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @abstractmethod
    def fazer_som(self):
        return f"O animal está fazendo um som."

    def movimentar(self):
        return f"O animal está se movimentando."

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"