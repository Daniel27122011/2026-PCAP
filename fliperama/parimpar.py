# =================================================
# Arquivo:    parimpar
# Disciplina: 2026-PCAP
# Aula:       20
# Autor:      Daniel G. souza
# Data:       2026.08.04
# Conceitos: 
# ===================================================

import random

def jogar_parimpar():
    print("--- INÍCIO DO JOGO: PAR OU ÍMPAR (5 RODADAS) ---")
    
    vitorias_jogador = 0
    vitorias_computador = 0
    
    for rodada in range(1, 6):
        print(f"\nRodada {rodada} de 5")
        
        # Escolha do jogador (Par ou Ímpar)
        escolha_jogador = ""
        while escolha_jogador not in ["P", "I"]:
            escolha_jogador = input("Escolha [P]ar ou [I]mpar: ").strip().upper()
        
        # Número do jogador
        try:
            num_jogador = int(input("Digite um número inteiro: "))
        except ValueError:
            print("Número inválido! Considerado 0 para esta rodada.")
            num_jogador = 0
            
        # Número do computador
        num_computador = random.randint(0, 10)
        print(f"O computador escolheu o número: {num_computador}")
        
        # Cálculo do resultado
        soma = num_jogador + num_computador
        resto = soma % 2
        
        print(f"Total: {soma} -> ", end="")
        if resto == 0:
            print("Deu PAR!")
            resultado = "P"
        else:
            print("Deu ÍMPAR!")
            resultado = "I"
            
        # Verificação do vencedor da rodada
        if escolha_jogador == resultado:
            print("Você venceu esta rodada!")
            vitorias_jogador += 1
        else:
            print("O computador venceu esta rodada!")
            vitorias_computador += 1
            
    # Resultado final do placar
    print("\n--- FIM DE JOGO ---")
    print(f"Placar Final: Você {vitorias_jogador} x {vitorias_computador} Computador")
    
    if vitorias_jogador > vitorias_computador:
        print("Parabéns! Você foi o grande vencedor!")
    else:
        print("O computador ganhou a melhor de 5!")

# Para testar este código sozinho, basta descomentar a linha abaixo:
# jogar_par_impar()