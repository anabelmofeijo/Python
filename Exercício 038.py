'''
Comparando números
'''
print("-="*20)
print("Comparando Números")
print("-="*20)
print("")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
print('')

if n1 > n2:
    print(f"\033[31m{n2}\033[m é maior!")
elif n2 > n1:
    print(f"\033[31m{n2}\033[m é o maior número!")
else:
    print("\033[31mOs números são iguais!\033[m")


# Dr. Stone
