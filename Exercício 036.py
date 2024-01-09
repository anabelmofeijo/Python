'''
Validando emprestimo
'''

casa = int(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
anos = int(input("Em quantos anos você vai pagar: "))
print("")
prestaçao = casa/(anos*12)
print(
    f"Para pagar uma casa de {casa} em {anos} anos a sua prestação mensal será: {prestaçao:.2f}")
minimo = salario*30/100


if prestaçao <= minimo:
    print("Emprestimo concedido!")
else:
    print("Emprestimo negado!")
