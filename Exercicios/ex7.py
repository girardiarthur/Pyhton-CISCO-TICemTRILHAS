nome = input("Digite seu nome: ")
livro = input("Digite o nome do livro: ")
totalPaginas = int(input("Digite o total de páginas do livro: "))
tempoPagina = int(input("Digite o tempo gasto para ler uma página (em segundos): "))
tempoTotal = (totalPaginas * tempoPagina) / 3600
print("==CALCULADORA DE TEMPO DE LEITURA==")
print(f"\n{nome}, você finalizará a leitura do livrro '{livro}' em aproximadamente {tempoTotal:.2f} horas.")