from util import red, white, cprint
from random import randint

a = randint(1, 100)
b = randint(1, 100)

answer = a + b

print("The answer to " + red(a) + " + " + red(b) + " = " + red(answer))

from os import system

go = input("Go back to main file? (Y/N)\n")

if go == "Y":
  system('clear')
  system('python3 main.py')