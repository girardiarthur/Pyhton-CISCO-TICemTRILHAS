nome = input("DIGITE SEU NOME:")
valorCompra = float(input("DIGITE O VALOR DA COMPRA:"))
desconto = float(input("DIGITE O VALOR DO DESCONTO:"))
descontoaplicado = (desconto / 100) * valorCompra
valorFinal = valorCompra - descontoaplicado
print(f"Olá {nome}, sua compra de R$ {valorCompra:.2f} foi confirmada!\nFoi aplicado um desconto de {desconto:.2f}%.\nO total final ficou em R$ {valorFinal:.2f}")