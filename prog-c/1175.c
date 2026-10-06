/*
* Disciplina: 2026-PCAP
* Problema  : beecrowd 1175 - Array Replacement 1
* Autor     : Daniel Gonçalves de Souza
* Data      : 2026.10.06
* LIAC      : Le 20 inteiros num vetor N. mostra o vetor com a ordem invertida. imprime cada posição no formato "n[0] = valor".
*/
#include <stdio.h>

int main() {
    int n[20], i;

    for (i = 0; i < 20; i++) {
        scanf("%d", &n[i]);
    }

    for (i = 0; i < 20; i++) {
        printf("N[%d] = %d\n", i, n[ 19 - i]);
    }

    return 0;
}