/*
programa: 1005.c
Data: 2026.09.22
Autor: Daniel
*/
#include <stdio.h>

int main() {
    double R, VOLUME;
    double pi = 3.14159;

    scanf("%lf", &R);

    VOLUME = (4.0 / 3) * pi * R * R * R;

    printf("VOLUME = %.3f\n", VOLUME);

    return 0;
}