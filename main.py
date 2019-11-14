from os import system
from util import red

print(red("1"), "-", red("Output using print"))
print(red("2"), "-", red("Simple Math using Pre-determined Integers and Variables"))
print(red("3"), "-", red("Simple Math using Input() and Variables\n"))

game = input("With this in mind, pick a variable from " + red("1") + " to " + red("3\n"))

if game.isdigit():
  if game == "1" or game == "2" or game == "3":
    system('clear')
    system('python3 remix' + game + '.py')
  else:
    print("I don't think", red(game), "is a number from 1-3.")