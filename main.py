from tipo_mamifero import Mamifero
from tipo_ave import Ave
from tipo_reptil import Reptil

def main():
    animais = []
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar Animal")
        print("2. Consultar Animais")
        print("3. Remover Animal")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tipo = input("Digite o tipo de animal (Ave, Mamifero, Reptil): ").strip().lower()
            nome = input("Digite o nome do animal: ")
            idade = int(input("Digite a idade do animal: "))
            
            if tipo == "ave":
                pode_voar = input("O pássaro pode voar? Digite(sim/não): ").strip().lower() == "sim"
                animal = Ave(nome, idade, pode_voar)
            elif tipo == "mamifero":
                tem_pelo = input("O mamífero tem pelo? (sim/não): ").strip().lower() == "sim"
                animal = Mamifero(nome, idade, tem_pelo)
            elif tipo == "reptil":
                tipo_de_pele = input("Digite o tipo de pele do réptil (escamas, outro): ").strip()
                animal = Reptil(nome, idade, tipo_de_pele)
            else:
                print("Tipo de animal desconhecido.")
                continue
            
            animais.append(animal)
            print("Animal cadastrado com sucesso!")
        
        elif opcao == "2":
            if not animais:
                print("Nenhum animal cadastrado.")
            else:
                for i, animal in enumerate(animais):
                    print(f"{i + 1}. {animal} - Som: {animal.fazer_som()} - Movimento: {animal.movimentar()}")
        
        elif opcao == "3":
            if not animais:
                print("Nenhum animal cadastrado para remover.")
            else:
                for i, animal in enumerate(animais):
                    print(f"{i + 1}. {animal}")
                indice = int(input("Digite o número do animal para remover: ")) - 1
                if 0 <= indice < len(animais):
                    removido = animais.pop(indice)
                    print(f"Animal removido: {removido}")
                else:
                    print("Número inválido.")
        
        elif opcao == "4":
            print("Encerrado...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()