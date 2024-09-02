# test_import.py
try:
    from animal_base import Animal
    from tipo_ave import Ave
    from tipo_mamifero import Mamifero
    from tipo_reptil import Reptil
    print("Importações bem-sucedidas!")
except ImportError as e:
    print(f"Erro de importação: {e}")