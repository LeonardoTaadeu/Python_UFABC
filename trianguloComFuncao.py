def areaTriangulo(a, b):
    return (a * b) / 2

base = float(input("Digite a base do triangulo: "))
altura = float(input("Digite a altura do triangulo: "))

resultado = areaTriangulo(altura, base)

print(f"A área do triangulo é: {resultado}")