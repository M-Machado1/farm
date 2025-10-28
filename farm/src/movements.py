
# movements.py
import json
import os
from datetime import datetime
from utils import get_valid_input

DATA_FILE = "data/movements.json"

def load_movements():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_movements(movements):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(movements, f, indent=4, ensure_ascii=False)

def add_movement():
    movements = load_movements()
    print("\n=== Registro de Movimentação ===")
    
    valid_types = ["venda", "colheita", "consumo"]
    while True:
        m_type = get_valid_input("Tipo (venda, colheita, consumo): ")
        if m_type.lower() in valid_types:
            break
        print("Erro: tipo inválido. Escolha entre venda, colheita ou consumo.")
    
    movement = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "type": m_type,
        "description": get_valid_input("Descrição: ")
    }
    movements.append(movement)
    save_movements(movements)
    print("Movimentação registrada!\n")

def list_movements():
    movements = load_movements()
    print("\n=== Lista de Movimentações ===")
    if not movements:
        print("Nenhuma movimentação registrada.")
        return
    for m in movements:
        print(f"{m['date']} | {m['type']} | {m['description']}")
    print()
