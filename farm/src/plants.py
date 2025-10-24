
# plants.py
import json
import os
from datetime import datetime, timedelta

DATA_FILE = "data/plants.json"

def load_plants():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def save_plants(plants):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(plants, f, indent=4, ensure_ascii=False)

def estimate_harvest(crop_type):
    if crop_type.lower() == "milho":
        return 120
    elif crop_type.lower() == "soja":
        return 110
    elif crop_type.lower() == "arroz":
        return 90
    else:
        return 60

def add_plant():
    plants = load_plants()
    print("\n=== Cadastro de Plantação ===")
    crop_type = input("Tipo de cultura: ")
    area = float(input("Área cultivada (ha): "))
    planting_date = input("Data de plantio (YYYY-MM-DD): ")
    days = estimate_harvest(crop_type)
    harvest_date = (datetime.fromisoformat(planting_date) + timedelta(days=days)).date().isoformat()
    plant = {
        "id": input("ID da plantação: "),
        "crop_type": crop_type,
        "area": area,
        "planting_date": planting_date,
        "harvest_date": harvest_date,
        "status": "planted"
    }
    plants.append(plant)
    save_plants(plants)
    print("Plantação cadastrada com sucesso!\n")

def list_plants():
    plants = load_plants()
    print("\n=== Lista de Plantações ===")
    if not plants:
        print("Nenhuma plantação cadastrada.")
        return
    for p in plants:
        print(f"ID: {p['id']} | Cultura: {p['crop_type']} | Área: {p['area']}ha | "
              f"Plantio: {p['planting_date']} | Colheita: {p['harvest_date']} | Status: {p['status']}")
    print()

def update_plant_status():
    plants = load_plants()
    id_p = input("ID da plantação: ")
    for p in plants:
        if p["id"] == id_p:
            print("Status atual:", p["status"])
            p["status"] = input("Novo status (planted, harvested, rotated, inactive): ")
            save_plants(plants)
            print("Status atualizado!\n")
            return
    print("Plantação não encontrada.\n")
