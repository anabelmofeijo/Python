'''
Faça um programa que leia um nome pelo teclado e mostre:
1- Quantas vezes aparece a letra A
2- Em que posição ela aparece pela primeira vez
3- Em que posição ela parec pela última vez
'''

frase = str(input("Digite uma frase: ")).upper().strip()
print ('A letra A aparece: ', frase.count('A'), 'vezes')
print('A primeira letra aparece na posição: ', frase.find('A')+1)
print('A última letra aparece na posição: ', frase.rfind('A')+1)
