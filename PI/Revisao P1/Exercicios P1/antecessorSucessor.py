def sucessor(a):
    return a + 1

def antecessor(b):
    return b - 1

num1 = float(input("Digite um numero: "))

resultadoSucessor = sucessor(num1)
resultadoAntecessor = antecessor(num1)

print(resultadoAntecessor)
print(resultadoSucessor)