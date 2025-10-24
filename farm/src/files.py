

# files.py
import os
import json

def ensure_files():
    os.makedirs("data", exist_ok=True)
    for filename in ["animals.json", "plants.json", "inputs.json", "movements.json"]:
        path = os.path.join("data", filename)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f)
