'''
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço a pagar da passagem, cobrando 0.50 por Km para viagens
de até 200 Km e 0.45 para viagens mais longas
'''

distância = float (input("Digite a distância em Km: "))

if distância <= 200:
    custo = distância*0.5
    print (f"O custo da viagem é de {custo}")
else:
    custo = distância*0.45
    print (f"O custo da viagem é de {custo}")

