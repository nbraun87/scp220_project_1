# IMPORTING MODULES
import math as m
from os import system, name
from time import sleep as sl

def pause():    
    input("press Enter key to continue...")

def print_menu():
    clearScreen()
    print("\nSelect from the following: \n " \
        "\t1. Power\n" \
        "\t2. SquareRoot\n" \
        "\t9. Exit")

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')

def squareroot():
    rad = float(input("Enter Radicand: "))
    result = m.sqrt(rad)
    print("The square root of {} is: {}".format(result, rad))
    pause()

def power():
    inA = float(input("Enter Base: "))
    inB = float(input("Enter Exponent: "))

    result = m.pow(inA, inB)
    
    print('{} raised to the power of {}: {}'.format(str(inA), str(inB), str(result)))
    pause()

def main():
    entry = '0'
    prompt = 'Please enter your choice: '
    animals = []
    while entry != '9':
        
        print_menu()    
        entry = input(prompt)

        if entry == '1':
            power()
            prompt = 'Please enter your choice: '

        elif entry == '2':
            squareroot()
            prompt = 'Please enter your choice: '

        elif entry == '9':
            clearScreen()
            print("Good Bye!")
            sl(2)
            clearScreen()
            break

        else:             
            prompt = "Incorrect choice, please enter a choice from above: "
            
main()