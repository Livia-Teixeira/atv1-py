#exercicio 7

pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Marcos", "idade": 39},
    {"nome": "Mariana", "idade": 22}
]


def extrair_nomes(lista):
    nomes = []
    for pessoa in lista:
        nomes.append(pessoa["nome"])
    return nomes


print(extrair_nomes(pessoas))
