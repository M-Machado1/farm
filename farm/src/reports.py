# reports.py
import json
import os
from datetime import datetime

# Define o caminho absoluto da pasta 'data'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def get_data_file(filename):
    return os.path.join(DATA_DIR, filename)

def load_json(file):
    if not os.path.exists(file):
        return []
    with open(file, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def generate_report():
    animals = load_json(get_data_file("animals.json"))
    plants = load_json(get_data_file("plants.json"))
    inputs = load_json(get_data_file("inputs.json"))

    report_path = get_data_file("report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("=== Relatório Geral da Fazenda ===\n")
        f.write(f"Data de geração: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")

        f.write(f"Total de animais: {len(animals)}\n")
        f.write(f"Total de plantações: {len(plants)}\n")
        f.write(f"Total de insumos: {len(inputs)}\n\n")

        f.write("Animais:\n")
        for a in sorted(animals, key=lambda x: x["id"]):
            f.write(f"  {a['id']} - {a['species']} - {a['status']}\n")

        f.write("\nPlantações:\n")
        for p in sorted(plants, key=lambda x: x["id"]):
            f.write(f"  {p['id']} - {p['crop_type']} - {p['status']}\n")

        f.write("\nInsumos:\n")
        for i in sorted(inputs, key=lambda x: x["name"]):
            f.write(f"  {i['id']} - {i['name']} - {i['quantity']} {i['unit']}\n")

    print(f"\nRelatório gerado em '{report_path}'\n")
