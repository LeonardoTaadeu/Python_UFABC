def conta_igual(listaA, listaB):
    contador = 0

    for i in range(len(listaA)):
        if listaA[i] == listaB[i]:
            contador += 1
        return contador