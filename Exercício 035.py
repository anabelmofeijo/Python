'''
Analisador de triângulos ( Saber se um triângulo é válido ou não)

'''
print("-="*20)
print("Analisando Triângulos")
print("-="*20)
print("")
l1 = float(input("Digite o L1: "))
l2 = float(input("Digite o L2: "))
l3 = float(input("Digite o L3: "))

if l1 < l2 + l2 and l2 < l1 + l2 and l3 < l1 + l2:
    print("Com estas medidas é possível formar um triângulo")
else:
    print("Não vai ser possível formar um triângulo")
