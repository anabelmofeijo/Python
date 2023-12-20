# Crie um programa que leia o comprimento do CA e Co. Calcule e mostre o valor da H

co = float(input("Digite o CO: "))
ca = float(input("Digite o CA: "))

h = (co**2 + ca**2)**(1/2)

print (f"O valor da hipotenusa é: {h:.1f}")

