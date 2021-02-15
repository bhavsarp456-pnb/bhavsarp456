from pyfiglet import figlet_format
from colorama import init, Fore, Back, Style
from termcolor import colored

init()

def generator_art(text, color):
    if color not in ('grey', 'red', 'green', 'yellow', 'blue', 'magneta', 'cyan', 'white'):
        color = 'white'
    ascii_art = figlet_format(text)
    print(colored(ascii_art, color))

text = input("Please enter the desired text:- ")
color = input("Please enter your desired color:- ")

generator_art(text,color)


