print("===CALCULADORA DE CHURRASCO===")
pessoas = int(input("Digite o número de pessoas: "))
quantidadeCarne = 0.3 * pessoas
quantiadeLinguiça = 0.2 * pessoas
quantidadeFrango = 0.15 * pessoas
custoCarne = 50 * quantidadeCarne
custoLinguiça = 28 * quantiadeLinguiça
custoFrango = 22 * quantidadeFrango
custoTotal = custoCarne + custoLinguiça + custoFrango
Contribuição = custoTotal / pessoas

print("\n===QUANTIDADES===")
print(f"Carne: {quantidadeCarne:.2f} kg - Linguiça: {quantiadeLinguiça:.2f} kg - Frango: {quantidadeFrango:.2f} kg")
print("\n===CUSTO TOTAL===")
print(f"Carne: R$ {custoCarne:.2f} - Linguiça: R$ {custoLinguiça:.2f} - Frango: R$ {custoFrango:.2f}")
print("\n==CUSTO TOTAL DO CHURRASCO==")
print(f"o Custo total do churrasco é de R$ {custoTotal:.2f}")
print(f"Cada pessoa deve contribuir com R$ {Contribuição:.2f}")
