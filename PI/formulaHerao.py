import math

def area_triangulo(a, b, c):

    semi_perimetro = (a + b + c) / 2

    return math.sqrt(semi_perimetro*(semi_perimetro - a)*(semi_perimetro - b)*(semi_perimetro - c))

lado1 = float(input(""))
lado2 = float(input(""))
lado3 = float(input(""))

resultado = area_triangulo(lado1, lado2, lado3)


