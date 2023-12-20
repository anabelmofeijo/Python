# 0rdem de apresentação de um trabalho


import random
n1 = str(input("Digite o 1º membro: "))
n2 = str(input("Digite o 2° membro: "))
n3 = str(input('Digite o 3° membro: '))
caixa = [n1,n2,n3]
random.shuffle(caixa)
print (f"A ordem de apresentação será: {caixa}")

