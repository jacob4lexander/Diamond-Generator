
from diamondfunc import build_diamond as build_ban
from os import system 

while (True):

    program_select = ('Enter a Program: ')
    length_select = ('Enter a Length between 11 and 51: ')

    program = input(program_select)
    if (program == ""):
        print("That isn't a program! Shutting down...")
        break
    length = input(length_select)

    if  ((int(length) % 2) != 0 and int(length) <= 101 and int(length) >= 11):
        build_ban(int(length), str(program))
    else:
        print("Please enter an odd number between 11 and 101 for length")

    input('Press enter to restart')

    system("cls")
    





