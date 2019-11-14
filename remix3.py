from util import red, white, cprint
from random import randint
from os import system

x1 = input("Pick a number: ")
y1 = input("Pick another number: ")

x = int(x1)
y = int(y1)

z = input("Pick an operator (multiply, divide, add, subtract): ")

answer = None

if z == "multiply":
  answer = x * y
  print("Answer:", answer)
elif z == "divide":
  answer = x / y
  print("Answer:", answer)
elif z == "add":
  answer = x + y
  print("Answer:", answer)
elif z == "subtract":
  answer = x - y
  print("Answer:", answer)
else:
  print("I didn't know " + z + " was an operator. Thank you for the knowledge.")

go = input("Go back to main file? (Y/N)\n")

if go == "Y":
  system('clear')
  system('python3 main.py')