import json
import os

DATA_FILE = "data/animals.json"

# ---------- Funções auxiliares ----------

def load_animals():
    """Carrega os dados do arquivo JSON (ou cria vazio se não existir)."""
    if not os.path.exists(DATA_FILE):
        save_animals([])
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_animals(animals):
    """Salva a lista de animais no arquivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(animals, f, indent=4, ensure_ascii=False)

# ---------- Funções principais ----------

def register_animal():
    """Cadastra um novo animal."""
    animals = load_animals()
    print("\n=== Cadastro de Animal ===")
    try:
        animal_id = input("ID do animal: ").strip()
        species = input("Espécie: ").strip()
        age = float(input("Idade (em meses ou anos): "))
        weight = float(input("Peso (kg): "))
        status = "active"

        # Verifica ID duplicado
        if any(a["id"] == animal_id for a in animals):
            print("❌ Já existe um animal com esse ID.")
            return

        animal = {
            "id": animal_id,
            "species": species,
            "age": age,
            "weight": weight,
            "status": status
        }

        animals.append(animal)
        save_animals(animals)
        print("✅ Animal cadastrado com sucesso!")

    except ValueError:
        print("❌ Entrada inválida! Certifique-se de digitar números corretamente.")

def list_animals():
    """Lista todos os animais cadastrados."""
    animals = load_animals()
    if not animals:
        print("\n⚠️ Nenhum animal cadastrado.")
        return
    print("\n=== Lista de Animais ===")
    for a in animals:
        print(f"ID: {a['id']} | Espécie: {a['species']} | Idade: {a['age']} | Peso: {a['weight']} kg | Status: {a['status']}")

def update_status():
    """Atualiza o status de um animal."""
    animals = load_animals()
    animal_id = input("\nDigite o ID do animal: ").strip()
    found = False
    for a in animals:
        if a["id"] == animal_id:
            print(f"Status atual: {a['status']}")
            print("1 - Ativo | 2 - Vendido | 3 - Falecido")
            opt = input("Escolha o novo status: ").strip()
            status_map = {"1": "active", "2": "sold", "3": "dead"}
            a["status"] = status_map.get(opt, a["status"])
            save_animals(animals)
            print("✅ Status atualizado com sucesso!")
            found = True
            break
    if not found:
        print("❌ Animal não encontrado.")

def search_animal():
    """Pesquisa animal por ID."""
    animals = load_animals()
    animal_id = input("\nDigite o ID do animal que deseja buscar: ").strip()
    found = next((a for a in animals if a["id"] == animal_id), None)
    if found:
        print(f"\n✅ Animal encontrado:")
        for k, v in found.items():
            print(f"{k.capitalize()}: {v}")
    else:
        print("❌ Nenhum animal com esse ID.")

def remove_animal():
    """Remove um animal do cadastro."""
    animals = load_animals()
    animal_id = input("\nDigite o ID do animal a ser removido: ").strip()
    updated = [a for a in animals if a["id"] != animal_id]
    if len(updated) < len(animals):
        save_animals(updated)
        print("🗑️ Animal removido com sucesso!")
    else:
        print("❌ Animal não encontrado.")

# ---------- Menu interno (para testes) ----------

def animals_menu():
    """Menu de gerenciamento de animais (para integração com main.py)."""
    while True:
        print("""
=== MENU ANIMAIS ===
1. Cadastrar animal
2. Listar animais
3. Atualizar status
4. Pesquisar animal
5. Remover animal
0. Voltar ao menu principal
""")
        op = input("Escolha uma opção: ").strip()
        if op == "1":
            register_animal()
        elif op == "2":
            list_animals()
        elif op == "3":
            update_status()
        elif op == "4":
            search_animal()
        elif op == "5":
            remove_animal()
        elif op == "0":
            break
        else:
            print("❌ Opção inválida!")
