import json
import requests

def req(url, dados):
    r = requests.post(url, json=dados)
    return r.json()


def escreve(dados,nome):
    with open(nome, 'a') as f:
        f.write(json.dumps(dados))

# lista dados injeção
url = 'https://www.ravenscanner3.com.br/api/sistemas/paginarmodelospormontadora'
dados = {
    "tipo": "otto",
    "montadora": "chevrolet",
    "count": 3000,
    "page": 1,
    "filtros": {}
}
# variações conforme lista abaixo de montadoras
# r = requests.post(url, json=dados)
# print(r.json())
# print(req(url,dados))


# # lista Montadoras
url = 'https://www.ravenscanner3.com.br/api/sistemas/listarmontadoras'
dados = {
    "megabloco": "otto"
}


# variações ( dieselleve, dieselpesado)


# lista sistemas de todos montadoras misturado
url = 'https://www.ravenscanner3.com.br/api/sistemas/paginarmodelos'

dados = {
    "tipo": "otto",
    "count": 30000,
    "page": 1,
    "filtros": {}
}


ciclos = ['dieselleve', 'dieselpesado','otto']


geral = []
for x in ciclos:
    dados = {
        "tipo": x,
        "count": 30000,
        "page": 1,
        "filtros": {}
    }

    z = req(url, dados)
    geral.append(z['dados'])

jsonString = json.dumps(geral)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

