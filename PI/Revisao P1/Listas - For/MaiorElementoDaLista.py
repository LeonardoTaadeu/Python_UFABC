def maior(lista):
    maior_elemento = float('-inf')

    for numero in lista:
        if numero > maior_elemento:
            maior_elemento = numero
    return maior_elemento