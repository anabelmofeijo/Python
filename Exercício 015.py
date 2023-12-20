'''
Escreva um programa que pergunte a quantidade de Km corridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar. Sabendo que o carro custa R$60 e R$0.15 por Km rodado

'''


distância = float (input("Digite a quantidade de Km corridos pelo carro: "))
dias = int(input("Digite a quantidade de dias pelos quais ele foi alugado: "))
total_a_pagar = distância*0.15 + dias*60
print(f"O total a pagar é de {total_a_pagar:.0f}.00Kz")
