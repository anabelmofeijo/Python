'''
Jogo com o computador de advinhação

'''
import random

n = int(input("Digite um número um número entre 0 a 5: "))
computador = random.randint(0,5)

if computador == n:
    print("Você venceu!")
else:
    print("Você perdeu")
