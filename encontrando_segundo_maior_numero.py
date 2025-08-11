#exercicio 3

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def segundo_maior_numero(lista):
    numeros_unicos = list(set(lista))
    numeros_unicos.sort(reverse=True)
    return numeros_unicos[1]

print("segundo maior número na lista numeros:", segundo_maior_numero(numeros))

