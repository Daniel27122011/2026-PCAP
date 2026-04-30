'''
problema: beecrowd | 1004
Data: 2026.04.23
Estudante: Daniel Gonçalves de Souza
'''
# Objetivo: Ler dois inteiros nas variaveis A e B, calcular o prouto em PROD e exibir o resultado

# --- ANÁLISE (LIAC)---
# Entrada: dois números inteiros, cada um em uma linha separada 
# Processamento: somar A + B e armazenar em PROD
# Sáida: exibir no formato exato "PROD = valor" (espaços ao redor do =, sem mensagens extras)

# int() converte o texto lido para número inteiro
# input() lê o valor fornecido (digitado ou pelo Beecrowd)
# int(input()) lê e converte em uma única instrução
A = int(input())
B = int(input())

# O enunciado especifica explicitamente as variáveis A, B e PROD - seguir á risca 
PROD = A * B 

# f- string: insere o valor de PROD dentro do texto com {}
# Atenção: espaço antes e depois do = é obrigatório conforme o enunciado
print(f"PROD = {PROD}")