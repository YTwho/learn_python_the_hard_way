# write a script that also accepts arguments
# import modules
from sys import argv
# read the WYSS section ffor how to run this
script, first, second, third = argv
# argv is the "argument variable", holds the arguments you pass to your python script when run it
# here rather than holding all arguments, it gets assigned to four vars you can work with
# ”Take whatever is inargv, unpack it, and assign itto all of these variables on the left in order.”

print("The script is called:", script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)

# to run this script, do: python ex13.py first 2nd 3rd

# for input(), input while script is running
# for argv, give inputs on the command line
