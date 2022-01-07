from os import system, name
from time import sleep as sl

def pause():
    input("Press Enter key to continue...")

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')

def addVehicle():
    pass

def editVehicle():
    pass

def deleteVehicle():
    pass

def displayInventory():
    pass

def print_menu():
    clearScreen()
    print("\nSelect from the following: \n " \
        "\t1. Add Vehicle\n" \
        "\t2. Edit Vehicle\n" \
        "\t3. Delete Vehicle\n" \
        "\t4. Show Inventory\n" \
        "\t9. Exit")

def main():
    usrInput = '0'
    prompt = 'Please enter your choice: '
    animals = []
    while usrInput != '9':
        
        print_menu()    
        usrInput = input(prompt)

        if usrInput == '1':
            addVehicle()
            prompt = 'Please enter your choice: '

        elif usrInput == '2':
            editVehicle()
            prompt = 'Please enter your choice: '

        elif usrInput == '3':
            deleteVehicle()
            prompt = 'Please enter your choice: '

        elif usrInput == '9':
            clearScreen()
            print("Good Bye!")
            sl(2)
            clearScreen()
            break

        else:             
            prompt = "Incorrect choice, please enter a choice from above: "
            
main()