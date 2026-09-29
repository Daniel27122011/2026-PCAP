/*
programa: 1005.c
Data: 2026.09.22
Autor: Daniel
*/
#include <stdio.h>

int main() {
    double A, B, C, media;

    // Leitura das três notas
    scanf("%lf %lf %lf", &A, &B, &C);

    // Cálculo da média ponderada
    media = (A * 2 + B * 3 + C * 5) / 10.0;

    // Impressão com uma casa decimal e quebra de linha (\n)
    printf("MEDIA = %.1f\n", media);

    return 0;
}