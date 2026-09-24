#FORMATAR MENSAGENS
# : - formata
# .2f - formata para 2 casas decimais
# f - float
#:< - alinha à esquerda
# :> - alinha à direita

"""
preco = 49.90
print(f"O preço do produto é: R$ {preco:.2f}") #imprime o preço formatado com 2 casas decimais
"""
"""
#CABEÇALHO
print(f"{'JOGADOR':<15} {'PONTOS':>10}") #imprime o cabeçalho da tabela com alinhamento à esquerda e à direita
print("-" * 26) #imprime uma linha de separação

#DADOS
jogador1 = "João" 
pontos1 = 1500
print(f"{jogador1:<15} {pontos1:>10}") #imprime os dados do jogador 1 com alinhamento à esquerda e à direita

jogador2 = "Maria"
pontos2 = 2000
print(f"{jogador2:<15} {pontos2:>10}") #imprime os dados do jogador 2 com alinhamento à esquerda e à direita
"""

#TESTE
print(f"{'PRODUTO':<15} {'PREÇO':>15}") #imprime o cabeçalho da tabela com alinhamento à esquerda e à direita
print("-" * 31) #imprime uma linha de separação

#dados
produto1 = "Mouse Gamer"
preco1 = 49.5
produto2 = "Teclado Mecânico RGB"
preco2 = 299.999
produto3 = "Monitor 4K"
preco3 = 1200.0
produto4 = "fone bluetooth"
preco4 = 89.75

print(f"{produto1:<15} {preco1:>15.3f}") #imprime os dados do produto 1 com alinhamento à esquerda e à direita
print(f"{produto2:<15} {preco2:>10.3f}")
print(f"{produto3:<15} {preco3:>15.3f}")
print(f"{produto4:<15} {preco4:>15.3f}")


#TESTEB
