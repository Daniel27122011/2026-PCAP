/*
Problema 1114 BeeCrowd
2026.09.29
Daniel G. souza
*/
#include <stdio.h>

int main() {
    int senha;
    
    while (scanf("%d", &senha) != EOF) {
        if (senha == 2002) {
            printf("Acesso Permitido\n");
            break;
        } else {
            printf("Senha Invalida\n");
        }
    }
    
    return 0;
}