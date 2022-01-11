from os import system, name, urandom
from time import sleep as sl
from Car import Car
import json

def pause():
    input("Press Enter key to continue...")

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')

def addVehicle():
    clearScreen()
    
    #Ask the user for the pieces of data needed
    #to create the new vehicle.
    print("Add new vehicle")
    make = input("Make: ")
    model = input("Model: ")
    vin = input("VIN: ")
    mileage = int(input("Mileage: "))
    price = float(input("Price: "))

    #Use a sentinel loop to build a list of features. 
    print("Enter features one at a time then press Enter.")
    print("Enter -1 to stop:")
    entry = input()
    features = []
    while entry != '-1':
        features.append(entry)
        entry = input()
    
    #Create new vehicle instance with data gathered.
    newCar = Car(make, model, vin, mileage, price, features)
    global vehicleInventory
    vehicleInventory.append(newCar)

def editVehicle():
    #MOVE TO PrepScreen function
    clearScreen()
    print("EEEEEEEEEE Edit Vehicle EEEEEEEEEE\n")

    global vehicleInventory
    index = None
    found = False
    displayInventory(1)
    #END MOVE TO
    Vin = int(input("VIN of vehicle to edit: "))
    for car in vehicleInventory:
        if Vin == car.vin:
            found = True
            index = vehicleInventory.index(car)
            print(car.display())
        
            #Create new vehicle instance with data gathered.
    if found: 
        print("Enter the new data for the vehicle: ")
        make = input("Make: ")
        model = input("Model: ")
        vin = input("VIN: ")
        mileage = int(input("Mileage: "))
        price = float(input("Price: "))

        #Use a sentinel loop to build a list of features. 
        print("Enter features one at a time then press Enter.")
        print("Enter -1 to stop:")
        entry = input()
        features = []
        while entry != '-1':
            features.append(entry)
            entry = input()
        vehicleInventory[index] = Car(make, model, vin, mileage, price, features)
    else:
        print("Vehicle Not Found!\nReturning to Main Menu")
        sl(3)

def deleteVehicle():
    clearScreen()
    print("DDDDDDDDDD Delete Vehicle DDDDDDDDDD\n")

    global vehicleInventory
    found = False
    index = None

    Vin = int(input("VIN of vehicle to delete: "))
    for car in vehicleInventory:
        if Vin == car.vin:
            found = True
            index = vehicleInventory.index(car)
            print(car.display())

    if found: 
        ch = input("Are you sure you want to delete? y n: ")
        if ch:
            print(f"Deleting: {vehicleInventory[index]}")
            vehicleInventory.pop(index)
        else:
            print("Vehicle NOT deleted. Returning to Main Menu...")
            sl(3)
#PARAMERER: op - option code. 0 = "return to main"
#                             1 = "just data"
def displayInventory(op = 0):
    global vehicleInventory
    if op == 0:
        for car in vehicleInventory:
            print(car.display())
        input("Press Enter to return to main...")
    else:
        for car in vehicleInventory:
            print(car.display())

def saveInventory():
    global vehicleInventory
    with open('data.dat', 'w') as fo:
        for car in vehicleInventory:
            if car.archive:
                fo.write(json.dumps(vehicleInventory))
                _ = input("Vehicle inventory saved.")
                break
        # for car in vehicleInventory:
        #     fo.write(json.dumps(car.__dict__))
        #     fo.write('\n')

def exportInventory():
    pass

def loadInventory():
    global vehicleInventory
    ch = input("Which data file to load? [data.dat]")
    if ch == "":
        ch = "data.dat"
    with open(ch, 'r') as fi:
        vehicleInventory = json.loads(fi)
        # for line in fi:
        #     readObject = json.loads(line)
        #     PersonObject = Person(readObject["fname"], readObject["lname"], readObject["data"])
        #     newListJson.append(PersonObject)

def print_menu():
    clearScreen()
    print("++++++++++ Welcome to Car Inventory Manager {:.1f} ++++++++++\n".format(appVersion))

    #TODO: Set color of option 5 to "Dark color" if archive is not needed. 
    # Question!?: checking vehInv list or global archive flag?
            
    print("\nSelect from the following: \n " \
        "\t1. Add Vehicle\n" \
        "\t2. Edit Vehicle\n" \
        "\t3. Delete Vehicle\n" \
        "\t4. Show Inventory\n" \
        "\t5. Export Inventory To File\n" \
        "\t6. Load Inventory From File\n" \
        "\t9. Exit")


appVersion = 1.5
appStartUp = True
vehicleInventory = []
vehicleInventory.append(Car("Volks", "Jetta", 123, 17000, 12000, ["AC", "Power Windows"]))
arch = False

def main():
    usrInput = '0'
    prompt = 'Please enter your choice: '
    
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

        elif usrInput == '4':
            displayInventory()
            prompt = 'Please enter your choice: '

        elif usrInput == '5':
            saveInventory()

        elif usrInput == '6':
            loadInventory()

        elif usrInput == '9':
            clearScreen()
            print("Good Bye!")
            sl(2)
            clearScreen()
            break

        else:             
            prompt = "Incorrect choice, please enter a choice from above: "
            
main()