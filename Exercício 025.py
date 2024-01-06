'''
Crie um programa que leia o nome completo de uma pessoa e diga se no seu nome
se encontra o nome silva
'''

nome = str(input("Digite o seu nome completo: ")).lower().title()

print("Seu nome tem Silva ? ", 'Silva' in nome)
