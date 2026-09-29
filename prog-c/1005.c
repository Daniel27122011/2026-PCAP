/*
programa: 1005.c
Data: 2026.09.22
Autor: Daniel
*/
#include <stdio.h>

int main() {
    double A, B, media;

    // Leitura dos valores de dupla precisão
    scanf("%lf", &A);
    scanf("%lf", &B);

    // Cálculo da média ponderada
    media = (A * 3.5 + B * 7.5) / 11.0;

    // Impressão com 5 casas decimais e quebra de linha (\n)
    printf("MEDIA = %.5f\n", media);

    return 0;