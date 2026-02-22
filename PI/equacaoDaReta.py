def coeficienteAngular(x1, x2, y1, y2):
    return (x1 - x2) / (y1 - y2)

def coeficienteLinear(y, coeficienteAngular, x):
    return y - (coeficienteAngular) * x

