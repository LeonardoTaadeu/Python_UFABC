peso = float(input())

altura = float(input())

imc = peso / (altura**2)

print("Para um peso de {} e altura de {}, o IMC calculado é {:.2f}.".format(peso, altura, imc))