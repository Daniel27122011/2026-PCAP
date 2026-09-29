/*
programa: 1002.c
Data: 2026.09.22
Autor: Daniel
*/
#include <stdio.h>

int main() {
    double raio, area;
    double pi = 3.14159;
    
    if (scanf("%lf", &raio) == 1) {
        area = pi * raio * raio;
        printf("A=%.4f\n", area);
    }
    
    return 0;
}