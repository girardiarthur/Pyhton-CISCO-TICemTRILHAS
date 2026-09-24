print("---divisor de contas DUBAR---")

#ENTRADA DE DADOS
valor_total = float(input("Digite o valor total da conta: "))
total_pessoas = int(input("a conta será dividida em quantas pessoas?: "))

#PROCESSAMENTO
valor_por_pessoa = valor_total / total_pessoas

#SAIDA DE DADOS
print("\n---RESULTADO---")
print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")
   
