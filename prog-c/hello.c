/* Comentário de Bloco
Programa: Hello.c
Data: 2026.09.22
Autor: Daniel Gonçalves de souza
 */

 // importa biblioteca padrão de entrada e saída
#include <stdio.h>

// defino a função principal do tipo int
int main(){
    // printf == Saída --> motra na tela  
    //"entre aspas == texto" 
    //comando se encerra com ;
    printf("Hello World!\n");

    // Receber 2 valores somar e mostrar o resultado
    int A=0, B=0;
    printf("digite o primeiro valor: ");
    scanf("%d", &A);
    printf("digite o segundo valor: ");
    scanf("%d", &B);
    int soma = A+B;
    printf("Soma: %d\n", soma);

    // indica que chegou ao fim a função == retornando 0
    return 0;
}

/*
para compilar ==
gcc <nome-do-arquivo> -o nome-do-programa

para executar ==
./nome-do-programa
*/