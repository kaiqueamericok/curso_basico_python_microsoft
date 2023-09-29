name = "Snake Sanders" 
planet = "Terra"
gravity = '7.77'

template = (f"Gravity Facts about {name}" "\n" "--------------------" "\n" f"Planet Name: {planet}" "\n" f"Gravity on {name}: {gravity} m/s2 "  )

print(template.format(name=name, planet=planet, gravity=gravity))

