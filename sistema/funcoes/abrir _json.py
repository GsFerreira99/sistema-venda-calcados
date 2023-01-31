import json

def dados_db():
    with open("../../dados.json", encoding='utf-8') as meu_json:
        return json.load(meu_json)[0]