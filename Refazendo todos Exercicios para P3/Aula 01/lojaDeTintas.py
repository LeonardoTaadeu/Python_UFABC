import math

area = float(input())

qntdLitros = area/12

qntdLatas = qntdLitros%18

valorLatas = qntdLatas*80

print("Para uma parede de área {}, você vai precisar de {} latas de tinta, com o custo de R$ {}.".format(area, qntdLatas, valorLatas))