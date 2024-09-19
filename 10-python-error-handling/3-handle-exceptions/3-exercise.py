Exercise: Raise exceptions
Exceptions allow a few patterns when they're used effectively. In this exercise, you'll ignore certain exceptions and fix problems where exceptions weren't used. Finally, you'll make a multiple-function program work better by handling exceptions and making decisions based on errors.

This exercise is broken into a series of steps. For each step you will be presented with the goal for the step, followed by an empty cell. Enter your Python into the cell and run it. The solution for each step will follow each cell.

Creating a utility to convert strings to boolean values
Imagine you are creating a program which will prompt the user for yes or no, which will be converted true or false. Because people will enter different values, you need to ensure the different possibilities are handled correctly. If an unknown response is given, the program should raise an error.

For purposes of this exercise, you'll use the values below for true and false. Run the cell to load the variables.


def str_to_bool(value):
    value = value.lower()
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError('Invalid entry')