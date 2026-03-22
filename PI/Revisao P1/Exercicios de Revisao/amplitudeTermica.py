def amplitude_termica(lista):
    numeroMaximo = lista[0]
    numeroMinimo = lista[0]

    for numeros in lista:
        if numeros > numeroMaximo:
            numeroMaximo = numeros
        if numeros < numeroMinimo:
            numeroMinimo = numeros
    return numeroMaximo - numeroMinimo