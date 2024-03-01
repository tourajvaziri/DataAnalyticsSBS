# Define two variables of type integer and give them values of your choice. 
# Then, write a conditional code:
# If the two variables are equal: prints ‘The variables are equal’
# If variable1 is double than variable2: prints: ‘The variable1 is double than variable2’
# If variable2 is double than variable1: prints: ‘The variable2 is double than variable1’
# And in any other case: prints the difference between them
>>> variable1 = 10
>>> variable2 = 5
>>> variable1 == variable2
False
>>> variable1 == 2 * variable2
True
>>> variable2 == 2 * variable1
False
>>> difference = abs(variable1 - variable2)
>>> print(f'The difference between the variables is: {difference}')
The difference between the variables is: 5
