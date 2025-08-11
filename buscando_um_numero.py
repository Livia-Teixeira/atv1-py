#exercicio 6
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def buscar_numero(numero, lista):
    return numero in lista

print("buscar número 42 na lista numeros:", buscar_numero(42, numeros))
