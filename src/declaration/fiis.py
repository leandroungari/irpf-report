class Fiis:
    def __init__(self, data):
        self.__data = data

    def generate(self):
        posicoes = self.descreverPosicoes()
        rendimentos = self.descreverRendimentos()
        return posicoes + rendimentos

    def descreverPosicoes(self):
        result = [
            "\n==============================",
            "\nDECLARAÇÃO DE BENS E DIREITOS",
            "\nCódigo: 73",
            "\n==============================",
        ]
        for item in self.__data["elementos"]:
            custo_medio_formatado = f'{item["precoMedio"]}'.replace('.', ',')
            custo_total_formatado = f'{item["precoMedio"]*item["quantidade"]}'.replace('.', ',')
            content = f'\n{item["quantidade"]} COTAS DE {item["nome"]} CÓDIGO DE NEGOCIAÇÃO B3 "{item["ticker"]}".\nCNPJ {item["cnpj"]}.\nCUSTO TOTAL DE R$ {custo_total_formatado}.\nCUSTO MÉDIO DE R$ {custo_medio_formatado}.\n'
            result.append(content.upper())
        return result

    def descreverRendimentos(self):
        result = [
            "\n==============================",
            "\nRENDIMENTOS ISENTOS E NÃO TRIBUTÁVEIS",
            "\nCódigo: 26",
            "\n==============================",
        ]
        for item in self.__data["elementos"]:
            rendimentos_formatado = f'{item["rendimentos"]}'.replace('.', ',')
            content = f'\nCNPJ Fonte Pagadora: {item["fontePagadora"]["cnpj"]}\nNome Fonte Pagadora: {item["fontePagadora"]["nome"]}\nDescrição: Rendimentos Recebidos do FII ({item["nome"]})\nValor: R$ {rendimentos_formatado}'
            result.append(content.upper())
        return result
