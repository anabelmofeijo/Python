# Faça um programa para dizer o sen cos e tan de um Ângulo

import math
a = int(input("Digite o valor do ângulo: "))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print (f"O seu Seno é: {sen:.2f}")
print (f'o seu cosseno é: {cos:.2f}')
print (f'A sua tangete é: {tan:.2f}')
