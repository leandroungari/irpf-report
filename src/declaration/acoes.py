class Acoes:
    def __init__(self, data):
        self.__data = data

    def generate(self):
        posicoes = self.descreverPosicoes()
        dividendos = self.descreverDividendos()
        return posicoes + dividendos

    def descreverPosicoes(self):
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

    def descreverDividendos(self):
        result = [
            "\n==============================",
            "\n==============================",
            "\nRENDIMENTOS ISENTOS E NÃO TRIBUTÁVEIS",
            "\nCódigo: 26 - Lucros e dividendos recebidos\n",
        ]
        for item in self.__data["elementos"]:
            rendimentos_formatado = f'{"{:.2f}".format(item["dividendos"])}'.replace('.', ',')
            content = f'\nCNPJ Fonte Pagadora: {item["cnpj"]}\nNome Fonte Pagadora: {item["nome"]}\nValor: R$ {rendimentos_formatado}\n'
            result.append(content.upper())
        return result
