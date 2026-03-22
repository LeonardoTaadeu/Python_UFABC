import math

def calcular_media(n1, n2, letra):
    if letra == "a":
        return (n1 + n2) / 2
    
    if letra == "g":
        return math.sqrt(n1 * n2)
    
    if letra == "h":
        return 2 / ((1/n1) + (1/n2))
    
    return 0

numero1 = float(input(""))
numero2 = float(input(""))

letraEscolhida = input("").lower()

resultado = calcular_media(numero1, numero2, letraEscolhida)

print(resultado)
    