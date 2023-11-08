from random import random
jogadores = []
parar = 'n'
while parar == 'n':
    entrada = str(input("Digite o nome dos jogadores (um de cada vez), ou, 'sair' p/ terminar: "))

    if entrada.lower() == 'sair':
        parar = 's'
    else:
        jogadores.append(entrada)

print(f"Lista de jogadores: {jogadores}")

