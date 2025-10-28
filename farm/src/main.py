"""
Equipe:
- Murilo Linhares Pereira Val Machado - 2025012542
- Fernando Levy Das Chagas - 2025012551
- João Victor Vasconcelos Cruz - 2025012515
- Martin Luthero Taaso Sousa e Silva - 2025012444
"""

from files import ensure_files
import animals
import plants
import inputs
import movements
import reports

def main_menu():
    ensure_files()
    while True:
        print("=== Sistema da Fazenda Digital ===")
        print("1. Animais")
        print("2. Plantações")
        print("3. Insumos")
        print("4. Movimentações")
        print("5. Relatórios")
        print("0. Sair")
        opc = input("Escolha: ")

        if opc == "1":
            animals_menu()
        elif opc == "2":
            plants_menu()
        elif opc == "3":
            inputs_menu()
        elif opc == "4":
            movements_menu()
        elif opc == "5":
            reports.generate_report()
        elif opc == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.\n")

def animals_menu():
    while True:
        print("\n--- Animais ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar status")
        print("0. Voltar")
        op = input("Escolha: ")
        if op == "1": animals.add_animal()
        elif op == "2": animals.list_animals()
        elif op == "3": animals.update_animal_status()
        elif op == "0": break

def plants_menu():
    while True:
        print("\n--- Plantações ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar status")
        print("0. Voltar")
        op = input("Escolha: ")
        if op == "1": plants.add_plant()
        elif op == "2": plants.list_plants()
        elif op == "3": plants.update_plant_status()
        elif op == "0": break

def inputs_menu():
    while True:
        print("\n--- Insumos ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Entrada de estoque")
        print("4. Saída de estoque")
        print("0. Voltar")
        op = input("Escolha: ")
        if op == "1": inputs.add_input()
        elif op == "2": inputs.list_inputs()
        elif op == "3": inputs.input_entry()
        elif op == "4": inputs.input_exit()
        elif op == "0": break

def movements_menu():
    while True:
        print("\n--- Movimentações ---")
        print("1. Registrar movimentação")
        print("2. Listar movimentações")
        print("0. Voltar")
        op = input("Escolha: ")
        if op == "1": movements.add_movement()
        elif op == "2": movements.list_movements()
        elif op == "0": break

if __name__ == "__main__":
    main_menu()
