#=================================================
# Disciplina: Pensamento computacional, Algoritimos e programação (PCAP)
# Projeto: jogo "Par ou Ímpar"
# Arquivo: par_impar.py
# Autor: Daniel Gonçalves de Souza
# Data: 25/06/2026
#==================================================
 
import random

pontos_jogador = 0
pontos_maquina = 0

for rodada in range(1, 6):
    print("========= RODADA", rodada, "==========")
    entrada = input("Sua jogada (par ou impar): ")
    jogada = entrada.lower().strip()

    numero_secreto = random.randint(0, 5)
    palpite = int(input("dedos_jogador (0 a 5): "))

    print(10 % 2)
    print(7 % 2)
    numero = 8
    if numero % 2 == 0:
        print("par")
    else:
        print("impar")
    opcoes = ["par", "impar"]
    if jogada not in opcoes:
        print("jogada inválida!")
jogada_maquina = random.randint(opcoes)
numero = 8
if soma % 2 == 0:
    print("par")
else:
    print("impar")
def quem_venceu(soma, aposta):
    if soma % 2 == 0:
        paridade = "par"
    else:
        paridade = "impar"
    if paridade == aposta:
        return "jogador"
    else:
        return "maquina"

print(10 % 2)
print(7 % 2)
numero = 8
if numero % 2 == 0:
    print("par")
else:
    print("impar")

print("Placar -> Você:", pontos_jogador, "| Máquina:", pontos_maquina)