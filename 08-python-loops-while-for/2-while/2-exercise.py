#In this exercise, you're creating an application that prompts a user to enter a list of planets. In a later #exercise, you'll add code that displays the list. For now, though, you'll create only the code that prompts the #user.

#This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, #followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow #each cell.

#Start by adding two variables, one for the input from the user, named new_planet, and another variable for the #list of planets, named planets.


while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done')

print(planets)