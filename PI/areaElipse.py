import math

def areaElipse(a, b):
    return a * b * math.pi

num1 = float(input("Digite o raio maior: "))
num2 = float(input("Digite o raio menor: "))

resultado = areaElipse(num1, num2)

print("A area do elipe e: {:.2f}".format(resultado))