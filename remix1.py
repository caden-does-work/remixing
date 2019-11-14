# Get the necessary modules for this remix.
from util import red, white
from random import randint

# Get a random integer from 1 to 100 twice, in order to add them together.
a = randint(1, 100)
b = randint(1, 100)

# Ask what they wish to be called, used below.
c = input("What is your name? ")

# Using the name from above, say hi in white and red.      
print(white("Hello, ") + red(c))

# State the calculation as they don't know it.
print(red(a) + " " + red(b))

# State it with text.
print(red(a), 'and', red(b))

# Nothing to see here
from os import system

go = input("Go back to main file? (Y/N)\n")

system('clear')
system('python3 main.py')