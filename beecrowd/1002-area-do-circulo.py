'''
problema: beecrowd | 1002
Data: 2026.05.07
Estudante: Daniel Gonçalves de Souza
'''
# Objetivo: efetuar o calculo da área, levando  valor de raio ao quadrado e multiplicando po n

# --- ANÁLISE (LIAC)---
# Entrada:  um número de ponto flutuante de dupla precisão (o raio R) 
# Processamento: aplicar a fórmula dA área do circulo
# Sáida: exibir no formato "AREA = " com 4 casas decimais 

# Leitura do raio como número decimal
R = float(input())

# Defina pi conforme o enunciado indica
pi = 3.14159

# Qual é a fórmula da área do circulo?
A = pi * R ** 2

# saída - obeseve o formato exato e o número de casas decimais no enunciado
print (f"A={A:.4f}")
