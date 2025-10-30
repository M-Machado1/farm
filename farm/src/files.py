import os
import json

# Define o caminho absoluto da pasta 'data'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

def ensure_files():
    os.makedirs(DATA_DIR, exist_ok=True)
    for filename in ["animals.json", "plants.json", "inputs.json", "movements.json"]:
        path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f)