import math

raio = float(input(""))

raioAoQuadrado = raio * raio

area = math.pi*raioAoQuadrado

print("Para um círculo de raio {:.2f}, a sua área é {:.2f}.".format(raio, area))