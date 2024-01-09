'''
Media do aluno
'''

print("-="*20)
print("Média final")
print('-='*20)
print("")

mac = float(input("Digite a sua MAC: "))
p1 = float(input("Digite a sua P1: "))
p2 = float(input("Digite a sua P2: "))


def calcular_media(mac, p1, p2):
    resultado = (mac + p1 + p2)/3
    return resultado


media = calcular_media(mac, p1, p2)

print(f"A sua média final é de: {media:.2f} valores")

if (media < 10):
    print("\033[31mEstás Reprovado\033[m")
elif (media >= 10 and media <= 14):
    print("\033[33mEstás aprovado com um desempenho razoável!\033[m")
elif (media > 14 and media <= 16):
    print("\033[34mEstás apto, com um desempenho muito bom!!\033[m")
elif (media > 16 and media <= 20):
    print("\033[32mEstás aprovado cientista!!!!\033[m")
else:
    print("\033[31mMédia Inválida!\033[m")

# Dr. Stone
