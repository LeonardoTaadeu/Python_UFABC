def conta_par(lista):
    numerosPares = 0

    for numeros in lista:
        if numeros % 2 == 0:
            numerosPares += 1
        return numerosPares