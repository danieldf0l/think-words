from random import random
jogadores = []
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
parar = 'n'
while parar == 'n':
    entrada = str(input("Digite o nome dos jogadores (um de cada vez), ou, 'sair' p/ terminar: "))

    if entrada.lower() == 'sair':
        parar = 's'
    else:
        jogadores.append(entrada)

print(f"Lista de jogadores: {jogadores}")

