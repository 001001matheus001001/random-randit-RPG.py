# Script feito por Matheus Silva
# 23:00 01/02/2018
# Programado em GNU/LINUX
# Projeto jogo RPG  ! ! !

import random

numero = random.randint(1, 3)

chute = int(input("digite de 1 a 3"))

while chute != numero:
    if chute > numero:
        print(chute, "numero é maior, tente novamente")
    if chute < numero:
        print(chute, "numero é menor, tente novamente")

    numero = int(input("seu chute:"))
print(chute,"Numero correto ")