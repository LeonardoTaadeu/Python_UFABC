def diferenca_quadrados(n):
    soma = 0
    somaQuadrados = 0

    for i in range(1, n+1):
        soma += i
        somaQuadrados += i ** 2
    quadradoSoma = soma ** 2

    return quadradoSoma - somaQuadrados
