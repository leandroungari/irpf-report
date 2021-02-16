class Acoes:
    def __init__(self, data):
        self.__data = data

    def generate(self):
        result = [
            "\n==============================",
            "\n31 - DECLARAÇÃO DE BENS E DIREITOS",
            "\n==============================",
        ]
        for item in self.__data["elementos"]:
            custo_medio_formatado = f'{item["precoMedio"]}'.replace('.', ',')
            custo_total_formatado = f'{item["precoMedio"]*item["quantidade"]}'.replace('.', ',')
            content = f'\n{item["quantidade"]} AÇÕES DE {item["nome"]} CÓDIGO DE NEGOCIAÇÃO B3 "{item["ticker"]}".\nCNPJ {item["cnpj"]}.\nCUSTO TOTAL DE R$ {custo_total_formatado}.\nCUSTO MÉDIO DE R$ {custo_medio_formatado}.\n'
            result.append(content.upper())
        return result
