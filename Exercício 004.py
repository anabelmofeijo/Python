#Dissecando um variável ou seja ver se é uma string ou não

n = input("Digite algo: ")
print (type(n))

print(f"É um número? {n.isnumeric()}")
print(f"É uma letra?  {n.isalpha()}")
print(f"É alfanumérico? {n.isalnum()}")




