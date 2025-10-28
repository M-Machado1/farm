
# animals.py
import json
import os
from utils import get_valid_input, get_valid_float




DATA_FILE = "data/animals.json"

def load_animals():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_animals(animals):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(animals, f, indent=4, ensure_ascii=False)

def add_animal():
    animals = load_animals()
    print("\n=== Cadastro de Animal ===")
    animal = {
        "id": get_valid_input("ID do animal: "),
        "species": get_valid_input("Espécie: "),
        "age": get_valid_float("Idade (em meses ou anos): "),
        "weight": get_valid_float("Peso (kg): "),
        "status": "active"
    }
    
    animals.append(animal)
    save_animals(animals)
    print("Animal cadastrado com sucesso!\n")

def list_animals():
    animals = load_animals()
    print("\n=== Lista de Animais ===")
    if not animals:
        print("Nenhum animal cadastrado.")
        return
    for a in animals:
        print(f"ID: {a['id']} | Espécie: {a['species']} | Idade: {a['age']} | Peso: {a['weight']}kg | Status: {a['status']}")
    print()

def update_animal_status():
    animals = load_animals()
    id_a = input("ID do animal: ")
    for a in animals:
        if a["id"] == id_a:
            print("Status atual:", a["status"])
            a["status"] = input("Novo status (active, sold, dead): ")
            save_animals(animals)
            print("Status atualizado!\n")
            return
    print("Animal não encontrado.\n")
