'''
Crie um programa que leia 3 números e diga qual é o maior e qual é o menor
'''

n1 = int (input("Digite o número: "))
n2 = int (input("Digite o número: "))
n3 = int (input("Digite o número: "))

if n1 > n2 and n1 > n3 :
    print (f"O maior valor é: {n1}")
if n2 > n1 and n2 > n3:
    print (f"O maior valor é: {n2}")
if n3 >n1 and n3 > n2:
    print(f"O maior valor é: {n3}")

if n1 < n2 and n1 < n3:
    print(f"O menor valor é: {n1}")
if n2 < n1 and n2 < n3:
    print(f"O menor valor é: {n2}")
if n3 < n1 and n3 < n2:
    print(f"O menor valor é: {n3}")

