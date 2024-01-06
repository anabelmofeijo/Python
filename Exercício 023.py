'''
Crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
separados
'''

num = int(input('Informe um número: '))
n = str(num)
print ('Unidade: ', n[3])
print ('Dezena: ', n[2])
print ('Centena: ', n[1])
print ('Milhar: ', n[0])
