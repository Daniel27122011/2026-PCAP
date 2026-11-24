# Fliperama em C++ (MeuApp v4.0)

## O que e
O programa funciona como um fliperama, permitindo cadastrar jogadores, listar os cadastrados e jogar Adivinhe o Número, contando as partidas de cada jogador.
Ele veio da versão anterior feita em C e foi adaptado para C++, utilizando recursos como vector, string e referências.

## Como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: contém o código do programa, o menu, os cadastros e o jogo.
- jogadores.csv: guarda o apelido do jogador na primeira coluna e a quantidade de partidas na segunda coluna.

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha) |
|---|---|---|
| guardar um jogador | strcpy(apelidos[qtd], novo) (1._) | apelidos. push_back(novo) (linha 95) |
| compararar apelidos | strcmp(...) == 0 (1._) | == (linha 65) |
| a funcao que cadastra | int cadastrar(..., int qtd) (1._) | void cadastrar(... &apelidos, ...) (linha 92)

## O que o C+ + decidiu pro mim
Em C, eu precisava controlar o tamanho dos vetores e copiar os textos usando strcpy().
Em C++, o vector cresce automaticamente com push_back(), e a string facilita o armazenamento e a comparação dos apelidos.

## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
|---|---|---|
| 1. Estrutura, compilacao e Git | C | fliperama.cpp, bibliotecas e função main() (linhas 1–177)|
| 2. Cadastro: vectors e referencia | C | Função cadastrar() e uso de vector com referências (linhas 87–97) |
| 3. Jogo e partidas | B | Função jogar_adivinhe() e atualização das partidas (linhas 110–120) |
| 4. Persistencia | B | Funções salvar() e carregar() (linhas 65-72) |
| 5. Documentacao e comparacao | C | README e tabela de comparação entre C e C++ |