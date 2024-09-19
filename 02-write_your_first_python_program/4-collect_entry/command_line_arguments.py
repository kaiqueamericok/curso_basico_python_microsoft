import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg 

#Explicando o código

import sys: Esta linha importa o módulo sys, que fornece acesso a várias funcionalidades relacionadas ao sistema, incluindo o acesso aos argumentos da linha de comando passados ao programa.

print(sys.argv): Aqui, sys.argv é uma lista que contém os argumentos passados para o programa a partir da linha de comando. A primeira posição (sys.argv[0]) geralmente contém o nome do programa em execução, e as posições subsequentes contêm os argumentos passados. Esta linha imprime toda a lista de argumentos, incluindo o nome do programa.

print(sys.argv[0]): Esta linha imprime o primeiro elemento da lista sys.argv, que é o nome do programa em execução. Em geral, isso exibirá o nome do arquivo Python que está sendo executado.

print(sys.argv[1]): Esta linha tenta imprimir o segundo elemento da lista sys.argv, que é o primeiro argumento passado ao programa a partir da linha de comando. Se nenhum argumento foi passado, isso resultará em um erro IndexError, pois a lista não terá elementos suficientes. É importante notar que sys.argv inclui o nome do programa como o primeiro elemento, então o primeiro argumento real estará na posição sys.argv[1].

