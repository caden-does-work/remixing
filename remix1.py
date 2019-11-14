from util import red, white, cprint
from random import randint

a = randint(1, 100)
b = randint(1, 100)
c = input("What is your name? ")
      
print(white("Hello, ") + red(c))

print(red(a) + " " + red(b))

print(red(a), 'and', red(b))

from os import system

go = input("Go back to main file? (Y/N)\n")

if go == "Y":
  system('clear')
  system('python3 main.py')