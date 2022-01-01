#VARIABLES
# Variables are mutable (changable)
#Not Stronly Typed

#Declaring and initializing variables. 
#string
name = "Nathan"
#int - integer
age = 34
#float
temp = 104.1

print(name)
print(age)
print(temp)
print()

name = "John"
age = 55
temp = 99.2

#dec laring a variable with a empty value using the keyword None.
nullvalue = None #null

print(nullvalue)

print(name)
print(age)
print(temp)
print()

nullvalue = "JohnJohn"
print(nullvalue)

#INPUT 
# accept data form the user's keyboard. 
# input(  ['string prompt']  )
# input returns a STRING of the entered data. 
# username = str(input("Username: "))

#CASTING FUNCTIONS
# Cast input string to integer
# age = int(input("Your Age: "))

# Cast input string to float
# temp = float(input("Enter the current temp outside: "))

#OUTPUT
print("Hello, " + name + ", how are you?")


Greeting = f"Hello, {name}, How are you doing?"
#interpolate using the f'' 
print(  Greeting  )

print(   'Hello {}, I am {} years old and it is {} degrees outside'.format(name, age, temp)   )


#COLLECTIONS
# LIST
# A list of pointer values that point to the beginning of different data values stored in memory (RAM).
#Lists use square brackets
#Data types are not required to be the same. 
#lists are zero-based indexes
daysOfWeek = ['Monday', "Tuesday", "Wednesday", 'Thursday']
myList = ['Janurary', 67, daysOfWeek]

# print(daysOfWeek)
print(myList)

print(myList[2][2])

#DICTIONARIES
# Uses keys in place of index numbers to reference element values. 
# Dictionaries use curly brackets
emp = {
    'fname': 'Nathan',
    'age':34,
    'skills': ['programming', 'video production', 'database admin'],
    'address': {'street': '23555 Rickard', 'state': 'OR'}
}

emp['address']['state'] = "TX"
print(f'Welcome, {emp["fname"]} this employee lives at {emp["address"]["state"]} ')
