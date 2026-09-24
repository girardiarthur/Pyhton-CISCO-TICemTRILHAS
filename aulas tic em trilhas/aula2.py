"""
Comandos de entrada
nome_do_heroi = input("Digite o nome do herói: ") #pergunta e armazena a resposta na variavel nome_do_heroi
print(f"O nome do herói é: {nome_do_heroi}")#imprime essa variavel na tela

"""
"""
TIPOS DE VARIAVEIS
INT - numeros inteiros
FLOAT - numeros decimais
STRING - texto
BOOLEAN - verdadeiro ou falso

"""

#CASTING OU CONVERSÃO DE TIPOS

#FORMA 1: RECEBE O TEXTO E CONVERTE PARA INTEIRO
#texto_idade = input("Digite a sua idade: ")
#idade = int(texto_idade) #converte o texto para inteiro

#FORMA 2: (MAIS USADA) CONVERTE DIRETO NA MESMA LINHA
idade = int (input("Digite a sua idade: ")) #converte o texto para inteiro

altura = float(input("Digite a sua altura: ")) #converte o texto para decimal

print(f"A sua idade é: {idade} e a sua altura é: {altura}") #imprime a idade e altura na tela19