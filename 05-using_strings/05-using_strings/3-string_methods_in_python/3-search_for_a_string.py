# Esse código em Python verifica se a string "Moon" está contida na frase "This text will describe facts and challenges with space travel" e imprime o resultado na tela. Se ele encontrar "Moon" irá resolver em True, se não encontrar, será false. 

print("Moon" in "This text will describe facts and challenges with space travel")

# Quando o método find não encontra a palavra, ele retorna "-1" quando encontra, ele retorna a posição onde se encontra o caractere

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

# O método .count() retorna o número total de ocorrências de uma determinada palavrada. 

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

# O método .lower. Converte letras maiúsculas em minúsculas. 

print("The Moon And The Earth".lower())

# O método .upper. Converte letras minúsculas em maiúsculas. 

print("The Moon And The Earth".upper())