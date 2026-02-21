totalSegundos = int(input("Digite um numero total de segundos: "))

horas = totalSegundos//3600

resto = totalSegundos%3600

minutos = resto//60

segundos = resto%60

print(horas)

print("{} segundos correspondem a {:02d}:{:02d}:{:02d}".format(totalSegundos, horas, minutos, segundos))