#exercicio 5
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def numeros_impares(lista):
    for num in lista:
        if num %2 !=0:
            print(num)

numeros_impares(numeros)            