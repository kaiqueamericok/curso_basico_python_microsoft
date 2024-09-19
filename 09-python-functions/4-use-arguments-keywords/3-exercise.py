In the prior exercise you created a report for a ship with three fuel tanks. What happens if the ship has multiple tanks? Keyword arguments can be a perfect solution for this type of a situation. With keyword arguments a caller can provide multiple values which your code can interact with.

This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

Create an updated fuel report function
Create a new function named fuel_report. The function will accept a keyword arguments parameter named fuel_tanks. Add the code to loop through the entries provided to generate the following output, where name is the name of the keyword argument and value is the value:

name: value
name: value

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')

main = 50
external = 100
emergency = 60