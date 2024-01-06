'''
Escreva um programa que  leia a velocidade de um carro, se ele ultrapassar os 80km/h mostre uma sms na tela
a  dizer que ele foi multado.
A multa vai custar 7.000 por cada km acima do limite
'''

velocidade = float (input("Digite a velocidade em Km/h: "))

multa = (velocidade-80)*7

if velocidade > 80:
    print ("Você foi multado!")
    print (f'O valor a pagar é de {multa:.0f}.00kz')
else:
    print ("Parabéns não foste multado!")
