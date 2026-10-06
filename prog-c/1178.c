/*
* Disciplina: 2026-PCAP
* Problema  : beecrowd 1178 - Array Fill 3
* Autor     : Daniel Gonçalves de Souza
* Data      : 2026.10.06
* LIAC      : Le um inteiro para N[0]. Cada posiacao seguinte vale o dobro da anterior, ate N[9]. Imprime as 10 posicoes "N[i] = valor". 
*/
#include <stdio.h>

int main() {
    double n[100];
    int i;

    scanf("%lf", &n[0]);

    for (i = 1; i < 100; i++) {
        n[i] = n[i - 1] / 2;
    }

    for (i = 0; i < 100; i++) {
        printf("N[%d] = %.4f\n", i, n[i]);
    }

    return 0;
}