'''
problema: beecrowd | 1003
Data: 2026.04.23
Estudante: Daniel Gonçalves de Souza
'''
# Objetivo: Ler dois inteiros nas variaveis A e B, calcular a soma em SOMA e exibir o resultado

# --- ANÁLISE (LIAC)---
# Entrada: dois números inteiros, cada um em uma linha separada 
# Processamento: somar A + B e armazenar em SOMA
# Sáida: exibir no formato exato "SOMA = valor" (espaços ao redor do =, sem mensagens extras)

# int() converte o texto lido para número inteiro
# input() lê o valor fornecido (digitado ou pelo Beecrowd)
# int(input()) lê e converte em uma única instrução
A = int(input())
B = int(input())

# O enunciado especifica explicitamente as variáveis A, B e SOMA - seguir á risca 
SOMA = A + B 

# f- string: insere o valor de SOMA dentro do texto com {}
# Atenção: espaço antes e depois do = é obrigatório conforme o enunciado
print(f"SOMA = {SOMA}")