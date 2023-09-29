# .replace()

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

# .lower()

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

# .join() esse método requer um objetvo iteravel, como uma lista.

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))