def coeficienteAngular(x1, x2, y1, y2):
    return (y1 - y2) / (x1 - x2)

def coeficienteLinear(y, coeficienteAngular, x):
    return y - (coeficienteAngular) * x

x1 = int(input("X1: "))
x2 = int(input("X2: "))

y1 = int(input("Y1: "))
y2 = int(input("Y2: "))

resultadoCoeficienteAngular = coeficienteAngular(x1, x2, y1, y2)
resultadoCoeficienteLinear = coeficienteLinear(y1, coeficienteAngular, x1)

print(resultadoCoeficienteAngular)
print(resultadoCoeficienteLinear)