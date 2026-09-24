print("====CALCULADORA DE META PESSOAL====")
meta = input("Digite sua meta pessoal: ")
valorNecessario = float(input("Digite o valor necessário para atingir sua meta: "))
salario = float(input("Digite o valor do seu salário: "))
despesas = float(input("Digite o valor das suas despesas: "))

resto = salario - despesas
reserva = resto * 0.30
valorMeta = resto - reserva
tempoNecessario = valorMeta / reserva
print(f"\nmeta: {meta}(R${valorNecessario:.2f})\nSalário: R${salario:.2f} - Despesas: R${despesas:.2f}")
print(f"\nSaldo após despesas: R${resto:.2f}\nReserva fixa(30%): R${reserva:.2f}\nValor disponivel para a meta: R${valorMeta:.2f}\nPrazo estimado para atingir a meta: {tempoNecessario:.2f} meses")