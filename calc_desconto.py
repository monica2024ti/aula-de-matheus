preco =float (input('qual o preço:'))
porcentagem = float(input('digite o desconto em porcentagem:'))
valor_desconto = (porcentagem * preco) / 100

preco_final = preco - valor_desconto
print(preco_final)