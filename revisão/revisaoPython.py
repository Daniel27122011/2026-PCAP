# Variáveis e tipos de dados: 
# variável é o espaço na memória do computador usado para armazenar dados como texto números valores lógicos cujo o conteúdo pode mudar durante a execução, e tendo 4 tipos de dados básicos int, float, string bool
'''
int = inteiro
numeros inteiros  que não tem casas decimais 
ex.: 10, -7, 0, 999

float = ponto flutuante
são os numeros  que tem casas decimais 
ex.: 3.14, -0.5, 9.0

str = string(texto)
 é uma sequencia de caracteres letras números, simbolos 
ex.: "Olá", 'Python', "123", "Bom" + "Dia"

bool = booleano
ele usa valores lógicos de verdadeiro ou falso 
ex.: True, False

quantidade = 10 # int
preço = 30.87 # float
produto = "caderno" # str
disponivel = True #bool

print(f"produto: {"Caderno"}")
print(f"Preço:R$ {30.87}")
print(f"quantidade: {10}")
print(f"disponivel: {True}")
'''
# Operadores:
# Os operadores são símbolos especiais que realizam operaçoes sobre valores e variáveis é como se fossem verbos na programação
'''
1. Operador de atribuição 
ele é um simbolo usado na programação para guardar um valor dentro de uma variável o mais conhecido é o (=)
ex.:
nome = "Python" # nome RECEBE "Python"
idade = 13 # idade RECEBE 13
x = 10 + 5 # x RECEBE o resultado de 10 + 5 

2. Operadores aritméticos
são os sìmbolos matemáticos usado para relizar contas básicas como adição, subtração, e multiplicação
adição: +
subtração: - 
multiplicação: *
divisão real: /
divisão inteira: // 
resto(módulo): %
potencia: **

3. Operadores Relacionais (comparação)
eles comparam os dois valores e retornam True ou False. Essenciais em condicionais(if).
== igual a: 5 == 5         True
!= diferente de: 5 != 3    True
> maior que: 5 > 3         True
< menor que: 5 < 3         False
>= maior ou igual: 5 >= 5  True
<= menor ou igual: 5 <= 3  True


4. Operadores Lógicos
Os operadores lógicos são usados para combinar ou inverter condições, permitindo que o programa tome decisões. eles retornam verdadeiro (true) ou falso (false). Ods principais são AND, OR e NOT (E, OU e NÃO).

operador | significado   | quando é True
--------------------------------------------
 and      | E lógico      | ambas verdadeiras 
 or       | OU lógico     | pelo menos uma verdadeira
 not      | NÃO (negacão) | inverte True -> False, False ->True
'''
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print (f"{numero} é PAR")
else:
    print(f"{numero} é ÍMPAR")

# Saída de Dados 
'''
É o processo de exibir ou apresentar as informações geradas por um programa ao usuário é o computador falando com a pessoa como (PRINT)

Formas de formatar a saída

método                 | sixtase                 | recomendado |
================================================================
f-string (Python 3.6+) | f"texto {variavel}"     | Sim         |
.format()              | "texto {}". format (var)| Ok          |
concatenação           | "texto " + str (var)    | Evite       |
vírgula no print       | print ("texto", var)    | Básico      |
exemplo:
'''
print ("Óla,  mundo!")     # Texto simples
print (42)                 # Número
print (3.14)               # Float
print (True)               # Booleano
print ()                   # Linha em branco

# Entrada de Dados
'''
é quando você fornece informaçoes ao computador é você conversando com computador

Métodos Úteis

  método   | O que faz                                    | Exemplo
=====================================================================
.strip()   | remove espaços extras nas pontas             | "Ana ".strip() -> "Ana"
.lower()   | converte para minúsculas                     | "SIM" .lower() -> "sim"
.upper()   | converte para maiúsculas                     | "pr".upper() -> "PR"
.title()   | primeira letra de cada palavra maiúscula     | "joão silva".title() -> "João Silva"
.replace() | substitui parte do texto                     | "3,14".replace(",", ".") -> "3.14"
.split()   | Dividde a string em uma lista pelo separador | "A B C".split() ->["A", "B", "C"]
.isdigit() | verifica se contém apenas dígitos            |"123".isdigit() -> True


# Estruturas condicionais
É um recurso da programação que permite ao programa tomar decisões. Ela verifica se uma condição é verdadeira ou falsa e, com base no resultado, escolhe qual ação deve ser executada.

sintaxe
1. if simples
if condição:
    # executa SE a condição for True
    bloco_de_código

2. if / else
if condição: 
    # excuta SE verdadeira
    bloco_verdadeiro
else:
    # executa SE falsa (caso contrário)
    bloco_falso

3. if / elif / else (múltiplas condições)
if condição_1:
    bloco_1
elif condição_2:
    bloco_2
elif condição_3:
    bloco_3
else:
    bloco_nenhuma # nenhuma condição anterior foi True

# Estrutura de Repetição
É um programa que permite executar o mesmo bloco de código várias vezes, enquanto uma condição for verdadeiro ou por um número determinado de repetiçoes. Ela evita o mesmo código manualmente e torna o programa mais eficiente.

for VS While

for                                           | While
===================================================================================
Quantidade de repetições conhecida            | Quantidade de repetições desconhecidas
Percorrer listas, strings, ranges             | Repetir até uma condição mudar
"Faça isso N vezes"                           | "Faça isso enquanto X for verdadeiro"
Ex.:imprimir 1 a 10, somar notas de uma lista | Ex.: menu, validação, jogo, senha
'''

#Exemplo
contador = 1

while contador <= 5:
    print(contador)
    contador += 1