import math

areaTamanho = float(input(""))

qntdLitros = areaTamanho/12

qntdLatas = qntdLitros/18

qntdLatasInteiras = math.ceil(qntdLatas)

int(qntdLatasInteiras)

qntdPreco = qntdLatasInteiras*80

print("Para uma parede de área {:.2f}, você vai precisar de {} latas de tinta, com o custo de R$ {:.2f}.".format(areaTamanho, qntdLatasInteiras, qntdPreco))
