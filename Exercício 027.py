'''
Faça um programa que leia o nome completo de uma pessoa e mostre na tela o primeiro e o último nome
'''

nome = str(input("Digite o seu nome completo: ")).strip().capitalize().split()
n = len(nome) - 1
print (f'O seu primeiro nome é: {nome[0]}')
print (f'O seu último nome é: {nome[n]}')

