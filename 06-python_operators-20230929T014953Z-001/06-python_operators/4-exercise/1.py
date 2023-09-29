# crie um aplicativo para trabalhar com números e entradas do usuário, iremos calcular a distância entre planetas

first_planet_input = input("Digite a distância do primeiro planeta em km: ")
second_planet_input = input("Digite a distância do segundo planeta em km: ")

# converta os dados que o usuário nos forneceu para string 

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

# subtraia first_planet de second_planet e converta o resultado em seu valor absoluto usando abs. Armazene o resultado em uma variável chamada distância_km. Em seguida, exiba o resultado na tela.

distance_km = first_planet - second_planet
print(abs(distance_km))
