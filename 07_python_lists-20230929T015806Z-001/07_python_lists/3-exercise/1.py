# crie uma variável chamada Planetas, adicione os planetas na lista (Menos Plutão) 

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print(planets)

# mostre a contagem dos planetas

number_of_planets = len(planets)

print("Aqui estão", number_of_planets, "Os planetas")

# adicione Plutão a lista

planets.append("Plutão")

print("Atualmente, aqui estão", len(planets), " Os planetas ")

print(planets[-1], "Este é o último planeta")