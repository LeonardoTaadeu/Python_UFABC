def celsius_fahrenheit(a):
    return (a*1.8) + 32

def media_celsius_fahrenheit(lista):
    total = 0
    contador = 0

    for temperatura in lista:
        total += celsius_fahrenheit(temperatura)
        contador += 1
    return total / contador