class Acoes:
    def __init__(self, data):
        self.__data = data

    def generate(self):
        posicoes = self.descreverPosicoes()
        dividendos = self.descreverDividendos()
        jscp_pagos = self.descreverJSCPPagos()
        jscp_nao_pagos = self.descreverJSCPNaoPagos()
        return posicoes + dividendos + jscp_pagos + jscp_nao_pagos

    def descreverPosicoes(self):
        result = [
            "\n==============================",
            "\n==============================",
            "\nDECLARAÇÃO DE BENS E DIREITOS",
            "\nCódigo: 31 - Posição Ações\n",
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
            if item["dividendos"] > 0:
                rendimentos_formatado = f'{"{:.2f}".format(item["dividendos"])}'.replace('.', ',')
                content = f'\nCNPJ Fonte Pagadora: {item["cnpj"]}\nNome Fonte Pagadora: {item["nome"]}\nValor: R$ {rendimentos_formatado}\n'
                result.append(content.upper())
        return result

    def descreverJSCPPagos(self):
        result = [
            "\n==============================",
            "\n==============================",
            "\nRENDIMENTOS ISENTOS E NÃO TRIBUTÁVEIS",
            "\nCódigo: 10 - Juros sobre capital próprio\n",
        ]
        for item in self.__data["elementos"]:
            if item["jscp"]["pagos"] > 0:
                rendimentos_formatado = f'{"{:.2f}".format(item["jscp"]["pagos"])}'.replace('.', ',')
                content = f'\nCNPJ Fonte Pagadora: {item["cnpj"]}\nNome Fonte Pagadora: {item["nome"]}\nValor: R$ {rendimentos_formatado}\n'
                result.append(content.upper())
        return result

    def descreverJSCPNaoPagos(self):
        result = [
            "\n==============================",
            "\n==============================",
            "\nDECLARAÇÃO BENS E DIREITOS",
            "\nCódigo: 99 - Juros sobre capital próprio não-pagos\n",
        ]
        for item in self.__data["elementos"]:
            if item["jscp"]["nao-pagos"] > 0:
                rendimentos_formatado = f'{"{:.2f}".format(item["jscp"]["nao-pagos"])}'.replace('.', ',')
                content = f'\nCRÉDITOS EM TRÂNSITO - JUROS SOBRE CAPITAL PRÓPRIO A RECEBER ({item["nome"]}) - ({item["cnpj"]})\nValor: R$ {rendimentos_formatado}\n'
                result.append(content.upper())
        return result
