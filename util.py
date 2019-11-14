from termcolor import colored

def cprint(message, color):
  return colored(message, color)

def red(string):
  return colored(string, 'red')

def white(string):
  return colored(string, 'white')
