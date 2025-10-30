# inputs.py
import json
import os
from utils import get_valid_input, get_valid_float

# Caminho do arquivo de dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "inputs.json")

# Função para carregar os insumos
def load_inputs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except:
            return []

# Função para salvar os insumos
def save_inputs(inputs):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(inputs, file, indent=4, ensure_ascii=False)

# Função para cadastrar novo insumo
def add_input():
    inputs = load_inputs()
    print("\n=== Cadastro de Insumo ===")
    insumo = {
        "id": get_valid_input("ID do insumo: "),
        "name": get_valid_input("Nome do insumo: "),
        "quantity": get_valid_float("Quantidade disponível: "),
        "unit": get_valid_input("Unidade de medida (kg, L, saco, etc): "),
        "category": get_valid_input("Categoria (feed, seed, fertilizer, medicine): ")
    }
    inputs.append(insumo)
    save_inputs(inputs)
    print("Insumo cadastrado com sucesso!\n")
    
# Função para listar insumos
def list_inputs():
    inputs = load_inputs()
    print("\n=== Lista de Insumos ===")
    if not inputs:
        print("Nenhum insumo cadastrado.")
        return
    for insumo in inputs:
        print(f"ID: {insumo['id']} | Nome: {insumo['name']} | "
              f"Qtd: {insumo['quantity']} {insumo['unit']} | "
              f"Categoria: {insumo['category']}")
    print()

# Função para registrar entrada de estoque
def input_entry():
    inputs = load_inputs()
    id_input = input("Informe o ID do insumo para entrada: ")
    for insumo in inputs:
        if insumo["id"] == id_input:
            add_qtd = float(input("Quantidade a adicionar: "))
            insumo["quantity"] += add_qtd
            save_inputs(inputs)
            print("Entrada registrada com sucesso!\n")
            return
    print("Insumo não encontrado.\n")

# Função para registrar saída de estoque
def input_exit():
    inputs = load_inputs()
    id_input = input("Informe o ID do insumo para saída: ")
    for insumo in inputs:
        if insumo["id"] == id_input:
            sub_qtd = float(input("Quantidade a retirar: "))
            if sub_qtd > insumo["quantity"]:
                print("Erro: quantidade insuficiente em estoque.\n")
                return
            insumo["quantity"] -= sub_qtd
            save_inputs(inputs)
            print("Saída registrada com sucesso!\n")
            return
    print("Insumo não encontrado.\n")
