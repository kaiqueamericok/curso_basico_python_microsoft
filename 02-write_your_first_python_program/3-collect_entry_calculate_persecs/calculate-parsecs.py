parsecs_input = input("Input number of parsecs: ")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")

# Explicação do Código: 

1.parsecs_input = input("Input number of parsecs: "): Esta linha solicita ao usuário que insira um número de parsecs. A função input() lê uma linha de entrada do usuário, e a mensagem entre as aspas serve como uma instrução para o usuário, explicando o que deve ser inserido. O valor inserido pelo usuário é armazenado na variável parsecs_input como uma string.

2.parsecs = int(parsecs_input): Nesta linha, o código converte a string parsecs_input em um número inteiro (int). Isso é necessário porque a entrada do usuário é lida como uma string, e se você deseja realizar cálculos matemáticos com ela, precisa convertê-la para um tipo numérico. O valor resultante é armazenado na variável parsecs.

3.lightyears = 3.26156 * parsecs: Aqui, o código calcula o equivalente em anos-luz (lightyears) com base no número de parsecs inserido pelo usuário. O valor 3.26156 é um fator de conversão aproximado que converte parsecs em anos-luz. O resultado do cálculo é armazenado na variável lightyears.

4.print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears"): Nesta linha, o código imprime a saída para o usuário. Ele usa a função print() para exibir uma mensagem que inclui o número de parsecs inserido pelo usuário, o valor equivalente em anos-luz (convertido em uma string usando str()), e a unidade "lightyears". O símbolo + é usado para concatenar (juntar) as diferentes partes da mensagem em uma única string que é exibida no console.