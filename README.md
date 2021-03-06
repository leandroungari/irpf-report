# IRPF Report

Essa ferramenta de linha de comando tem como intuito auxiliar o processo de preenchimento dos campos da Declaração de Imposto de Renda de Pessoa Física.

Inicialmente o foco desse projeto está relacionado a investimentos em renda física e renda variável.

## Como executar

Após clonar o projeto, você deve instalar as dependências. Para isso você deve ter a última versão do Python e do `pip` instalados:

```bash
pip3 install -r requirements.txt
```

Na sequência, você iniciar o ambiente virtual:

```bash
source ./bin/active
```

E, por fim, executar o programa:

```bash
python src/main.py -i filename.json
```

Onde `filename.json` é o arquivo que descreve os dados para geração do relatório.

O formato atual é o seguinte:

```
{
  "produtos": {
    "31": {
      "elementos": [
        {
          "ticker": "ENBR3",
          "nome": "Energias do Brasil S.A.",
          "cnpj": "03.983.431/0001-03",
          "quantidade": 17,
          "precoMedio": 19.18
        },
        {
          "ticker": "ENBR3",
          "nome": "Energias do Brasil S.A.",
          "cnpj": "03.983.431/0001-03",
          "quantidade": 17,
          "precoMedio": 19.18
        },
        ...
      ]
    },
    "73": {
      "elementos": [
        {
          "ticker": "XPML11",
          "nome": "XP MALLS FDO INV IMOB FII",
          "cnpj": "28.757.546/0001-00",
          "quantidade": 7,
          "precoMedio": 125.56,
          "rendimentos": 6.79,
          "fontePagadora": {
            "nome": "BTG PACTUAL SERVIÇOS FINANCEIROS SA DTVM",
            "cnpj": "59.281.253/0001-23"
          }
        },
        ...
      ]
    }
  }
}
```

**Importante**
> Atualmente, está disponível o preenchimento dos dados quanto a ações e fundos imobiliários.

Como saída, será gerado um arquivo `data/output.txt` contendo o relatório gerado, conforme o exemplo abaixo.

```
==============================
==============================
DECLARAÇÃO DE BENS E DIREITOS
Código: 31

17 AÇÕES DE ENERGIAS DO BRASIL S.A. CÓDIGO DE NEGOCIAÇÃO B3 "ENBR3".
CNPJ 03.983.431/0001-03.
CUSTO TOTAL DE R$ 326,06.
CUSTO MÉDIO DE R$ 19,18.

17 AÇÕES DE ENERGIAS DO BRASIL S.A. CÓDIGO DE NEGOCIAÇÃO B3 "ENBR3".
CNPJ 03.983.431/0001-03.
CUSTO TOTAL DE R$ 326,06.
CUSTO MÉDIO DE R$ 19,18.

==============================
==============================
DECLARAÇÃO DE BENS E DIREITOS
Código: 73

7 COTAS DE XP MALLS FDO INV IMOB FII CÓDIGO DE NEGOCIAÇÃO B3 "XPML11".
CNPJ 28.757.546/0001-00.
CUSTO TOTAL DE R$ 878,92.
CUSTO MÉDIO DE R$ 125,56.

==============================
==============================
RENDIMENTOS ISENTOS E NÃO TRIBUTÁVEIS
Código: 26

CNPJ FONTE PAGADORA: 59.281.253/0001-23
NOME FONTE PAGADORA: BTG PACTUAL SERVIÇOS FINANCEIROS SA DTVM
DESCRIÇÃO: RENDIMENTOS RECEBIDOS DO FII (XP MALLS FDO INV IMOB FII)
VALOR: R$ 6,79

...
```