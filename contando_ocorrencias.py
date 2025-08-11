#exercicio 9

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]


def contar_ocorrencias(lista, valor):
    return lista.count(valor)

print("quantas vezes o número 2 aparece na lista numeross:", contar_ocorrencias(numeros, 2))
