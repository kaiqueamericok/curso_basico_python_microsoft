#The previous exercise, you created code to prompt users to enter a list of planet names. In this exercise, you'll #complete the application by writing code that displays the planet names one by one.

#This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, #followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow #each cell.

#The first cell contains the code from the prior exercise, without the print statement. Run the cell and provide a #list of planets. (Enter a planet name and select "Submit". For each new entry, overtype the previous entry and #select "Submit".)

# Run this cell and provide a list of planets

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet or done if done')