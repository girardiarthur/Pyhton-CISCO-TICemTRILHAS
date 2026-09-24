print("==AÇAITERIA==")


pedidoP = int(input("Digite a quantidade de pedidos do tamanho P: "))
pedidoM = int(input("Digite a quantidade de pedidos do tamanho M: "))
pedidoG = int(input("Digite a quantidade de pedidos do tamanho G: "))

acaiP = 13.50
acaiM = 15
acaiG = 17.50

desconto = int(input("Digite o valor do desconto em %: "))
descontoAplicado = desconto / 100 * (pedidoP * acaiP + pedidoM * acaiM + pedidoG * acaiG)
total = (pedidoP * acaiP) + (pedidoM * acaiM) + (pedidoG * acaiG) - descontoAplicado
print(f"Desconto de {desconto:.2f}% aplicado.\nTotal R$ {total:.2f}")