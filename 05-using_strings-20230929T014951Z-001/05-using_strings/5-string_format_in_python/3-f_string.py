# as variáveis são passadas entre chaves. 

mass_percentage = "1/6"
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")

# é possível usar expressões dentro das chaves, para representar o valor 1/6 como um percentual com uma casa decimal, posso usar a função round() diretamente

print(round(100/6, 1))

# também não precisa atribuir um valor a uma variável com antecedência:

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

# posso aplicar o método .title na variável subject. 

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)