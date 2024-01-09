'''
Conversão de bases (Octal, hexadecimal,binário)

'''
print("-="*20)
print("Conversão de bases")
print("-="*20)
print("")
n = int(input("Digite um número inteiro: "))
print('Escolha a base para conversão:')
print('[1] converter para binário')
print('[2] converter para octal')
print('[3] converter para hexadecimal')
print("")

opcao = int(input("Digite a sua opção: "))

if opcao == 1:
    print(f'{n} em Binário é igual a: {bin(n)[2:]}')
elif opcao == 2:
    print(f"{n} em octal é igual a {oct(n)[2:]}")
elif opcao == 3:
    print(f'{n} em hexadecimal é igual a: {hex(n)[2:]}')
else:
    print("\033[31mOPÇÃO INVÁLIDA\033[m")


# Dr. Stone
