# Gets the required methods.
from util import red
from random import randint

# Get two numbers from 1 to 100.
a = randint(1, 100)
b = randint(1, 100)

# Get an answer with those randomly generated numbers.
answer = a + b

# Print the answer.
print("The answer to " + red(a) + " + " + red(b) + " = " + red(answer))


# Nothing
from os import system

go = input("Go back to main file? (Y/N)\n")

system('clear')
system('python3 main.py')