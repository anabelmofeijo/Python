# fazer sorteio de alunos

import random
n1 = str(input("Digite o 1º nome: "))
n2 = str(input("Digite o 2° nome: "))
n3 = str(input('Digite o 3° nome: '))
caixa = [n1,n2,n3]
resultado = random.choice(caixa)
print (f"O Aluno escolhido foi: {resultado}")

