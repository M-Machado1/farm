
# movements.py
import json
import os
from datetime import datetime

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
    movement = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "type": input("Tipo (venda, colheita, consumo): "),
        "description": input("Descrição: ")
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
