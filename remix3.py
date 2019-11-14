from os import system

# Pick two numbers.
x1 = input("Pick a number: ")
y1 = input("Pick another number: ")

# Make those two numbers into integers to be used in addition.
x = int(x1)
y = int(y1)

# Get the answer and then print it.
answer = x + y

print(x, "+", y, "is", answer)


# When done, allow them to input anything to return to the main.py.
go = input("Input anything to return to the main file.\n")

system('clear')
system('python3 main.py')