class Acoes:
    def __init__(self, data):
        self.__data = data

    def generate(self):
        result = [
            "\n==============================",
            "\n==============================",
            "\nDECLARAÇÃO DE BENS E DIREITOS",
            "\nCódigo: 31\n",
        ]
        for item in self.__data["elementos"]:
            if item["quantidade"] > 0 :
                custo_medio_formatado = f'{"{:.2f}".format(item["precoMedio"])}'.replace('.', ',')
                custo_total = item["precoMedio"]*item["quantidade"]
                custo_total_formatado = f'{"{:.2f}".format(custo_total)}'.replace('.', ',')
                content = f'\n{item["quantidade"]} AÇÕES DE {item["nome"]} CÓDIGO DE NEGOCIAÇÃO B3 "{item["ticker"]}".\nCNPJ {item["cnpj"]}.\nCUSTO TOTAL DE R$ {custo_total_formatado}.\nCUSTO MÉDIO DE R$ {custo_medio_formatado}.\n'
                result.append(content.upper())
        return result
