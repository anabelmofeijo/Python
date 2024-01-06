'''
Criar um programa que pergunte a cidade em que o usuária nasceu se ele ou não começa com a palavra santo
'''

n = str (input("Digite o nome da cidade que você nasceu: ")).upper().strip()
nome_com_split = n.split()
nome = nome_com_split[0]
print('SANTO' in nome)
