# Pedra-Papel-Tesoura

Jogo de Pedra-Papel-Tesoura feito em python na disciplina PCAP (Aula17).
Você joga contra o computador  em uma melhor de 5 rodadas, com placar.

## Como jogar 
1. Abra o terminal na pasta do jogo.
2. Rode: python ppt.py
3. A cada rodada, digite pedra, papel ou tesoura.
4. Ao fim das 5 rodadas, o rograma mostra o placar final

## Como funciona (resumido)
A cada rodada o computador sorteia uma jogda (random.choice) e lê a sua.
O texto digitado é limpo (.lower().strip()) e validado (in) antes de comparar.
Uma sub-rotina decide quem venceu e o programa soma os pontos das 5 rodadas.

## O que eu pratiquei
-Strings e métodos de texto: .lower() e .strip() para limpar o que foi digitado
- Validação com in: aceitar só pedra, papel ou tesoura
- Comparação de textos (==): descobrir empate e vitórias
- random.choice: sortear a jogada da máquina
- Repetição (for): jogar as 5 rodadas e manter o placar
- Sub-rotinas (def/return): isolar a regra do jogo
 
## Autoavaliação
Conceito pretendido: [ A / B / C / D ]

Justificativa       
- O jogo funciona Roda corretamente a melhor de 5: ppt.py, linhas 1 a 44 
- Trabalho com texto normaliza, valida e compara corretamente: ppt.py (.lower().strip(), in, ==)
- Documentação e Git README presente; código no GitHub: este README + commits no GitHub
- Extensão/originalidade entrego o jogo base (nível C): ppt.py, linha (o que eu criei - níveis B/A)
- Autoavaliação justificada declaro o conceito com justificativa simples ou parcial
Autor: [Daniel gonçalves de souza]