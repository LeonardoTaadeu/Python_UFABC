def jokenpo(j1, j2):
    if j1 == j2:
        return 0

    if (j1 == "pedra" and j2 == "tesoura") or (j1 == "tesoura" and j2 == "papel") or (j1 == "papel" and j2 == "pedra"):
        return 1
    
    return 2

jogador1 = input("Jogador 1: ").lower()
jogador2 = input("Jogador 2: ").lower()

resultado = jokenpo(jogador1, jogador2)

print("O jogador campeao foi o ",resultado)

