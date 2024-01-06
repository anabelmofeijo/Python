'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, Calcule aumento de 10%
Para inferiores ou iguais, aumento de 15%

'''

print("***********************************************")
print("****************Aumento************************")
print("***********************************************")
print("")

salario = float(input("Digite o seu salário: "))

# Cálculo

aumento_10 = salario + (10/100 * salario)
aumento_15 = salario + (15/100 * salario)

if salario <= 1250:
    print(f"O seu novo salário é: {aumento_15}")
else:
    print(f"O seu novo salário é: {aumento_10}")


# Dr. Stone
