from os import system

x1 = input("Pick a number: ")
y1 = input("Pick another number: ")

x = int(x1)
y = int(y1)

answer = None
print(int(x + y))

go = input("Go back to main file? (Y/N)\n")

system('clear')
system('python3 main.py')