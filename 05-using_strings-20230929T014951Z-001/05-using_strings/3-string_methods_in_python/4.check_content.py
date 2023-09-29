temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':') # usando o método split, para dividir a string "temperatures"  com base no ":"
print(parts)
print(parts[-1]) # o -1 retorna o último item 


# loop

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():  # começa o loop for, e percorre cada "item" de "mars_temperature.split():" 
    if item.isnumeric(): # Se encontrar um "item" numerico, retorna true 
        print(item)

# .startswith()

print("-70".startswith('-'))

# .endswith() 

if "30 C".endswith("C"):
print("This temperature is in Celsius")