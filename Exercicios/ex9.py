print("==análise de performance==")
pista = float(input("Digite o tamanho da pista em metros: "))
voltas = int(input("Digite o número de voltas: "))
tempo = float(input("Digite o tempo gasto em segundos para completar a primeira volta: "))

distanciaTotal = (pista * voltas) / 1000
tempoFinal = (tempo * voltas) / 60

print(f"\nAnálise Preditiva Concluída\n\nDistância total a ser percorrida: {distanciaTotal:.2f} km\nPrevisão de conclusão: {tempoFinal:.2f} minutos")