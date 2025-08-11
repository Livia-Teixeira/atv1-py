#exercicio 14
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def media_lista(lista):
    if len(lista) == 0: 
        return 0
    soma = sum(lista)          
    quantidade = len(lista)    
    media = soma / quantidade   
    return media

print("média dos números da lista numeros:", media_lista(numeros))
