import mysql.connector
from mysql.connector.errors import OperationalError


# print("Type Control C or 99 to exit")
# number = 1
# while number != 99:
#    number = int(input("Enter a number: "))
#    print("You entered:", number)



# # Manual error detection and handling:
# print("Type Control C or 99 to exit")
# number = 1
# while number != 99:
#    string = input("Enter a number: ")
#    if string.isnumeric(): #PROBLEM, Wont Validate negative numbers
#        number = int(string)
#    else:
#        print("ERROR: this is not a number: ")



# Manual error detection and handling with overriden isNumberic:
# def isNumeric(str):
#     if str[0] == '-':
#         if str[1:len(str)].isnumeric():
#             return True
#         else:
#             return False
#     else: 
#         return str.isnumeric()

# print("Type Control C or -1 to exit")
# number = 1
# while number != -1:
#    string = input("Enter a number: ")
#    if isNumeric(string): 
#        number = int(string)
#    else:
#        print("ERROR: this is not a number: ")



# Exception Handling:
# print("Type Control C or 99 to exit")
# number = 1
# while number != 99:
#     try: 
#         number = int(input("Enter a number: "))
#     except ValueError:
#         print("ERROR: This is not a number!")

# ? Why use exception handling over manual error handling?
# A: When the error doesn't happen often/is truly exception and unexpected. 
# Why: when performing manual error handling, more code must be executed in order
# to do so. Therefore, relying on Exception handling allows your program to 
# execute less code under 'normal' circumstances 
# AND you are able to customize how the program handles the situation and provide
# detailed error messages or log entries. 

def connectDB():
    return mysql.connector.connect(host="localhost", 
                               user='root',
                               password='toucan7',
                               database = 'elt')

conn = connectDB()

input('Press enter to execute query command...')
try:
    cursor = conn.cursor()
    cursor.execute("Select * from client")
    results = cursor.fetchall()
    for x in results:
        print(x)
except OperationalError:
    print("EXCEPTION: Connection to Database was lost!")
except: 
    print("An error occured.")
    
