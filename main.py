from os import system
from util import red, white

remixes = ["Output using print", "Simple Math using Pre-determined Integers and Variables", "Simple Math using Input() and Variables"]

for i in remixes:
  print(red(remixes.index(i) + 1) + " - " + red(i))

game = input(white("With this in mind, pick a variable from ") + red("1") + white(" to ") + red(str(len(remixes)) + "\n"))

if game.isdigit():
  if int(game) > 0 and int(game) < len(remixes) + 1:
    system('clear')
    system('python3 remix' + game + '.py')
  else:
    print("I don't think", red(game), "is a number from " + red("1") + " - " + red(str(len(remixes) + 1)))