
# reports.py
import json
import os
from datetime import datetime

def load_json(file):
    if not os.path.exists(file):
        return []
    with open(file, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []

def generate_report():
    animals = load_json("data/animals.json")
    plants = load_json("data/plants.json")
    inputs = load_json("data/inputs.json")

    with open("data/report.txt", "w", encoding="utf-8") as f:
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

    print("\nRelatório gerado em 'data/report.txt'\n")
