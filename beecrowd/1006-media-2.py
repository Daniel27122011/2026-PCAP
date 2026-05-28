'''
problema: beecrowd | 1006
Data: 2026.04.14
Estudante: Daniel Gonçalves de Souza
'''
# Objetivo: Ler duas notas com pesos diferentes e calcular a média ponderada

# --- ANÁLISE (LIAC)---
# Entrada: duas notas de ponto flutuante A e B(cada uma em uma linha)
# Processamento: comisão = média ponderada = (A * 3.5 + B * 7.5) / 11
# Sáida: EXIBIR NO FORMATO exato "MEDIA = valor" com 5 casas decimais

# float (input()) lê valores monetários (podem ter casas decimais)
A = float(input())
B = float(input())    
C = flaot(input())
# Nota A tem peso 3.5 e nota B TEM PESO 7.5
# A soma dos pesos é 11 - divide-se por 11 para obter a média ponderada
media = (A * 2 + B * 3 + C * 5) / 10

# :. 5f dentro da f-string formata o número com exatamente 5 casas decimais
# O enunciado exige espaço antes e depois do = - seguir á risca
print(f"MEDIA = {media:.1f}")