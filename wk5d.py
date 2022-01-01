# RECURSION
# Recursion is two-part:
# 1. recursion breaks a complex task into small repetitive actions.
# 2. recursion is a call to a function that calls itself repeatedly until
#    there is no data left. 

aListOfNumbers = [23, 65, 27, 9, 63, 66]

def popPrint( list ):
    for x in list:
        print(x, end=" ")
    print()
    if(len(list) > 0):
        list.pop()
        popPrint(list)
    else:
        print("Finished processing entries!")

popPrint(aListOfNumbers)
print('\n\n')


# SCOPE
# The area to which a piece of code has access. 
# Global  vs  Local
# Global is accessible everywhere.
# Local is only accessible within the same scope, or from inner scopes.

var1 = 55

def func1():
    print('func1')
    print(var1) #closure - reaching outward to access outer scope.
    var2 = 88
    print(var2)

func1()
#print(var2) #FAILURE - closure only goes in 1 direction.

# 'globals()' System function
# Returns a Dictionary of global variables. 
var1 = 66

def func2():
    print('func2')
    var1 = 99
    print(var1)
    print(globals()['var1'])
    print(var1 + 1)
    # func1(55)

func2()

#global keyword
var1 = 123

def func3():
    print('func3')
    var2 = 987
    print(var2)
    global var1
    var1 += 1
    print(var1 )

func3()
print(var1)

# OVERLOADED FUNCTIONS... 
# Multiple functions sharing the same name, but different parameter lists. 
# One method of writing functions that can operate on varying amounts of
# arguments.

'''function makeEmployee (fname, lname, empid)
{
    Emp1 = {'fname': fname, 'lname': lname, 'empid': empid}
    return Emp1
}

function makeEmployee (lname, empid)
{
    Emp1 = {'fname': 'CHANGEME', 'lname': lname, 'empid': empid}
    return Emp1
}
function makeEmployee (fname, lname)
{
    Emp1 = {'fname': fname, 'lname': lname, 'empid': 888}
    return Emp1
}'''



# No Such Thing in Python!!!
# Instead, we use 'default parameters'

# DEFUALT Parameters
def mkEmployee(lname, empid = 999, fname = "John"):
    return {'fname': fname, 'lname': lname, 'empid': empid}

print(mkEmployee('braun'))
print(mkEmployee('braun', 123))
print(mkEmployee('braun', 345, 'nathan'))

# KEYWORD Arguments
# Order of arguments does not matter.
print(mkEmployee(fname="Bradley", lname="McLennon", empid="777"))

# ARBITRARY Agruments
# Received ? number of arguments as a Tuple
def addNumbers(*nums):
    total = 0
    print(nums)
    for x in range(len(nums)): #Must use range and len, tuples are not iterable.
        total += nums[x]
    return total

print()
print(addNumbers(22, 44, 11))

# ARBITRARY KEYWORD Arguments
# Received key/value pair list as a Dictionary


