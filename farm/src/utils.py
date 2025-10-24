
# Arquivo auxiliar para centralizar o tratamento de erros 
from datetime import datetime

def get_valid_input(prompt, required=True):
    """
    Pede uma string ao usuário, tratando entradas vazias.
    Trata entradas inválidas.
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        if not required:
            return None
        # Exibir mensagens claras
        print("Erro: Esta entrada não pode ser vazia.")

def get_valid_float(prompt):
    """
    Pede um número float, tratando ValueError .
    """
    while True:
        value_str = get_valid_input(prompt)
        try:
            return float(value_str)
        except ValueError:
            
            print("Erro: Por favor, digite um número válido (ex: 10.5).")

def get_valid_int(prompt):
    """
    Pede um número inteiro, tratando ValueError .
    """
    while True:
        value_str = get_valid_input(prompt)
        try:
            return int(value_str)
        except ValueError:
            
            print("Erro: Por favor, digite um número inteiro válido (ex: 10).")

def get_valid_date(prompt):
    """
    Pede uma data no formato YYYY-MM-DD, tratando ValueError .
    Formato ISO "YYYY-MM-DD".
    """
    while True:
        date_str = get_valid_input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            
            print("Erro: Formato de data inválido. Use YYYY-MM-DD.")