# https://www.udemy.com/python-beyond-the-basics-object-oriented-programming/learn/v4/t/lecture/2599392?start=120

# Example of pdb module for real time debugging in the terminal

import pdb

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in values:
    mysum = 0
    mysum = mysum + val
    pdb.set_trace()

print mysum

# type n to go to the next line (keep you in the current context, does not enter to a function)
# type the name of the variables to see the values
# type s to get into functions
# type l shows you the code and the position in it
# type h for help
