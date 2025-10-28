# plants.py
import json
import os
from datetime import timedelta
from utils import get_valid_input, get_valid_float, get_valid_date

DATA_FILE = "data/plants.json"

def load_plants():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Aviso: plants.json inválido ou corrompido. Iniciando com lista vazia.")
            return []

def save_plants(plants):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(plants, f, indent=4, ensure_ascii=False)

def load_harvest_times():
    file_path = "data/harvest_times.json"
    if not os.path.exists(file_path):
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Aviso: harvest_times.json inválido ou corrompido. Usando valores padrão.")
            return {}

def estimate_harvest(crop_type):
    harvest_times = load_harvest_times()
    key = crop_type.lower().strip()
    days = harvest_times.get(key, 60)
    if key not in harvest_times:
        print(f"Aviso: Cultura '{crop_type}' não encontrada em harvest_times.json. Usando valor padrão de {days} dias.")
    return days

def add_plant():
    plants = load_plants()
    print("\n=== Cadastro de Plantação ===")

    while True:
        crop_type = get_valid_input("Tipo de cultura: ").strip()
        try:
            float(crop_type)
            print("Aviso: O tipo de cultura não deve ser apenas numérico. Digite um nome (ex.: milho, soja, arroz).")
            continue
        except ValueError:
            pass
        if not crop_type:
            print("Erro: o tipo de cultura não pode ser vazio.")
            continue
        break

    area = get_valid_float("Área cultivada (ha): ")
    planting_date = get_valid_date("Data de plantio (YYYY-MM-DD): ")

    days = estimate_harvest(crop_type)
    harvest_date = (planting_date + timedelta(days=days)).isoformat()

    plant = {
        "id": get_valid_input("ID da plantação: ").strip(),
        "crop_type": crop_type,
        "area": area,
        "planting_date": planting_date.isoformat(),
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
        print(
            f"ID: {p.get('id', '')} | Cultura: {p.get('crop_type', '')} | Área: {p.get('area', 0)}ha | "
            f"Plantio: {p.get('planting_date', '')} | Colheita: {p.get('harvest_date', '')} | Status: {p.get('status', '')}"
        )
    print()

def update_plant_status():
    plants = load_plants()
    plant_id = get_valid_input("ID da plantação: ").strip()

    for plant in plants:
        if plant.get("id") == plant_id:
            print("Status atual:", plant.get("status", ""))

            status_options = {
                "1": "planted",
                "2": "harvested",
                "3": "rotated",
                "4": "inactive"
            }

            print("\nEscolha o novo status:")
            for option_number, status_name in status_options.items():
                print(f"{option_number} - {status_name}")

            while True:
                choice = get_valid_input("Opção: ").strip()
                if choice in status_options:
                    plant["status"] = status_options[choice]
                    save_plants(plants)
                    print("Status atualizado!\n")
                    return
                print("Erro: escolha inválida. Digite um número de 1 a 4.")

    print("Plantação não encontrada.\n")
