# Desconto

preço = float(input("Digite o preço do produto: "))

valor_de_desconto = (preço*5)/100
desconto = preço - valor_de_desconto
print (f"O produto que custa {preço}.00Kz com um desconto de 5% vai custar {desconto:.2f}.00KZ")
