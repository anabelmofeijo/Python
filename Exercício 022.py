'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
1- O nome com tds as letras maiúsculas
2- O nome com tds as letras menúsculas
3- Quantas letras ao todo (sem considerar os espeços)
4- Quantas letras tem o primeiro nome.
'''

nome = str(input("Digite o seu nome Completo: ")).strip()
nome1 = nome.split()
nome2 = nome1[0]
print('1º', nome.upper())
print('2º', nome.lower())
print('3º', len(nome))
print('4º', len(nome2))

