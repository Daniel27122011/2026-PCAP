#=================================================
# Arquivo   :ppt.py (pasta fliperama)
# Conceitos :jogo com modulo , lista como tabela nome, função com retorno, operador  para dar a volta
# Base      :jogo da Aula 17(Atividade 11)
# Autor     :Daniel goncalves de souza
# Data      :2026.08.11
#==================================================

# importa função randint da biblioteca randdom, sorteia um número inteiro aletório em um intervalo definido
from random import randint

# importa as funçoes titulo e linha do arquivotelas.py
from telas import titulo, linha

# importa a função ler_opcao que validda a entrada do usuario do arquivo modulos.py
from modulos import ler_opcao

# lista com PEDRA == posição 0 ; PAPEL == 1 ; TESOURA == 2
JOGADAS = ['PEDRA', 'PAPEL', 'TESOURA']

# DEFINE O GANHADOR
def quem_vence(jogador, computador):
        if jogador == computador:
             return 'empate'
        if jogador == (computador + 1) % 3:
            return 'jogador'
        return 'computador'


def mostrar_jogadas():
      print('[0] Pedra')
      print('[1] Papel')
      print('[2] Tesoura')
      linha()

def jogar_ppt():
    titulo('PEDRA - PAPEL - TESOURA')

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao('Sua jogada', ['0', '1', '2']))
        computador = randint(0, 2)

        print('Você Jogou ' + JOGADAS[jogador] + '.')
        print('Computador Jogou ' + JOGADAS[computador] + '.')

        resultado = quem_vence(jogador, computador)

        if resultado == 'empate':
              print('Empate! Nínguem venceu!')
        elif resultado == 'jogador':
              pontos_jogador += 1
              print('Você Venceu essa rodada!')
        elif resultado == 'computador':
            pontos_computador += 1
            print('Computador Venceu essa rodada!')

        linha()
        print(f'Placar: jogador {pontos_jogador} x {pontos_computador} Computador')
        linha()

    if pontos_jogador > pontos_computador:
         titulo('YOU WIN!')
    else:
         titulo('YOU LOSE!')

