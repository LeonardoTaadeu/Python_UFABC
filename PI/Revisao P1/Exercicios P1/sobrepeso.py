def calcula_imc(peso, altura):
    return peso / (altura ** 2)

def conta_sobrepeso(pesos, alturas):
    contador = 0
    for i in range(len(pesos)):
        imc = calcula_imc(pesos[i], alturas[i])
        if imc > 25:
            contador += 1
        return contador