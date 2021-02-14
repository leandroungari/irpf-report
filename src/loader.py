import pandas as pd

def welcome():
    print("=======================================")
    print("===== FERRAMENTA DE PREENCHIMENTO =====")
    print("=====           IRPF              =====")
    print("=======================================\n")

def load_settings():
    filename = input("Insira o nome do arquivo de dados: ")
    return pd.read_json(f"data/{filename}")


