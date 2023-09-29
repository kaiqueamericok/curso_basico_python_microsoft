# Vamos explorar como podemos criar um programa que possa calcular a distância entre dois planetas. 

first_planet = 149597870
second_planet = 778547200

# Comece adicionando o código para subtrair first_planet de second_planet e armazene o resultado em uma variável chamada distance_km. Exiba o valor na tela.

distance_km = second_planet - first_planet

print(distance_km)

# Em seguida, adicione o código para converter distância_km em milhas dividindo-o por 1,609344 
# (a diferença aproximada entre milhas e quilômetros) e armazene o resultado em uma variável chamada distância_mi. Exiba o valor na tela.

distance_mi = distance_km / 1.609344

print(distance_mi)