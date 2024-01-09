'''
Alistamento Militar

'''

from datetime import date
print("-="*20)
print("Alistamento Militar")
print("-="*20)
print("")


ano = int(input("Digite a sua data de nascimento: "))


# Cálculo
ano_actual = date.today().year
idade = ano_actual - ano
alistamento = idade - 18
ano_alistamento = ano_actual - alistamento
alistamento_menor = 18 - idade
print(f'Quem nasceu em {ano} tem {idade} anos')

if idade == 18:
    print("Já podes se alistar")
elif idade < 18:
    print('Não podes se alistar. Ainda és menor de idade!')
    print(f'Falta {alistamento_menor} ano/s para o seu alistamento')
else:
    print(f"Você já deveria ter se alistado a {alistamento} anos")
    print(f"Seu alistameto foi em {ano_alistamento}")

# Dr. stone
