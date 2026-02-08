import math

areaMetrosQuadrados = float(input())

qntdMetrosParaPintar = areaMetrosQuadrados/12 

#Latas para pintar Print 1

qntdLatasParaPintar = areaMetrosQuadrados/18

qntdLatasInteira = math.ceil(qntdLatasParaPintar) #Quantidade de Latas

int(qntdLatasInteira)

precoLatasInteiras = qntdLatasInteira*80

#Latas para pintar Print 2

qntdGaloesParaPintar = areaMetrosQuadrados/3.6

qntdGaloesInteiro = math.ceil(qntdGaloesParaPintar) #Quantidade de Galoes

int(qntdGaloesInteiro)

precoGaloesInteiros = qntdGaloesInteiro*25

#Juncao de Latas x Galoes

latasParaUsar = math.floor(areaMetrosQuadrados/18)

restoLatas = areaMetrosQuadrados - (latasParaUsar*18)

quantidadeGaloes = math.ceil(restoLatas/3.6)

precoLatasJuncao = latasParaUsar*80

precoGaloesJuncao = quantidadeGaloes*25

precoTotal = precoLatasJuncao+precoGaloesJuncao

print(f"Para uma parede de área {areaMetrosQuadrados:.2f}, você vai precisar de {qntdLatasInteira} latas de 18 litros, com o custo de R$ {precoLatasInteiras:.2f}.")
print(f"Para uma parede de área {areaMetrosQuadrados:.2f}, você vai precisar de {qntdGaloesInteiro} latas de 3,6 litros, com o custo de R$ {precoGaloesInteiros:.2f}.")
print(f"Para uma parede de área {areaMetrosQuadrados:.2f}, você vai precisar de {latasParaUsar} latas de 18 litros e {quantidadeGaloes} latas de 3,6, com o custo de R$ {precoTotal}.")