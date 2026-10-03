/*
Problema 1043 BeeCrowd
2026.09.29
Daniel G. souza
*/
#include <stdio.h>

int main() {
    float a, b, c;

    scanf("%f %f %f", &a, &b, &c);

    if (a < b + c && b < a + c && c < a + b) {
        float perimetro = a + b + c;
        printf("Perimetro = %.1f\n", perimetro);
    } else {
        float area = ((a + b) * c) / 2.0;
        printf("Area = %.1f\n", area);
    }

    return 0;
}