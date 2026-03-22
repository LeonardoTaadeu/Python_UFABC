def celsius_fahrenheit(a):
    return (a*1.8) + 32

def amplitude_termica_fahrenheit(lista):
    fahrenheitMaximo = celsius_fahrenheit(lista[0])
    fahrenheitMinimo = celsius_fahrenheit(lista[0])
    
    for temperatura in lista:
        f = celsius_fahrenheit(temperatura)
        if f > fahrenheitMaximo:
            fahrenheitMaximo = f
        if f < fahrenheitMinimo:
            fahrenheitMinimo = f
    return fahrenheitMaximo - fahrenheitMinimo

    