import json
from os import read

class Person:
     def __init__(self, fname, lname, data = {}):
          self.fname = fname
          self.lname = lname
          self.data = data

list1 = []
list1.append(Person("Nathan", "Braun", {'mother':'ada','father':'bob'}))
list1.append(Person("Robert", "Kane", {'mother':'edie','father':'wayne'}))


#SAVE DATA WITH WRITE AND LOOPS
#AND PRINT DATA TO SEE DATA STRUCTURE
print("The following data is being loaded into the textfile:")
with open('datafileWL.txt', 'w') as fo:
    for x in list1:
        print()
        for y in x.__dict__.keys():
            if type(x.__dict__[y]) is dict:
                for z in x.__dict__[y].keys():
                    print('\t', z, x.__dict__[y][z])
                    fo.write("{} {} ".format(z, x.__dict__[y][z]))
            else:
                print(y, x.__dict__[y])
                fo.write('{} {} '.format(y, x.__dict__[y]))
        fo.write('\n')


newList = []
#LOAD DATA USING READ AND LOOPS
with open('datafileWL.txt', 'r') as fi:
    for line in fi:
        words = line.split()
        newList.append(Person("{} {}".format(words[1], words[2]), {words[3]: words[4], words[5]: words[6]}))

# print from the new list to prove we successfully loaded
# the data.
print("\nThe following was read from file into newList:")
for x in newList:
    print()
    for y in x.__dict__.keys():
        if type(x.__dict__[y]) is dict:
            for z in x.__dict__[y].keys():
                print('\t', z, x.__dict__[y][z])
        else:
            print(y, x.__dict__[y])
    print()



#SAVE DATA TO FILE USING JSON.DUMPS() TO TXT FILE
print("Writing data to datafileJSON.txt using JSON.DUMPS():")
with open('datafileJSON.txt', 'w') as fo:
    for x in list1:
        fo.write(json.dumps(x.__dict__))
        fo.write('\n')


newListJson = []
#LOAD DATA FROM FULE USING JSON.LOAD
with open('datafileJSON.txt', 'r') as fi:
    for line in fi:
        readObject = json.loads(line)
        PersonObject = Person(readObject["fname"], readObject["lname"], readObject["data"])
        newListJson.append(PersonObject)
# CAUTION: json.loads() created generic dict objects! You must manually pass the 
#          the data through the class constructor in order to return it to it's 
#          original self. i.e. a Person object, as opposed to a Dict object. 

print("\nThe following was read in from datafilesJSON using JSON:")

for x in newListJson:
    print()
    for y in x.__dict__:
        if type(x.__dict__[y]) is dict:
            for z in x.__dict__[y].keys():
                print('\t', z, x.__dict__[y][z])
        else:
            print(y, x.__dict__[y])

    
print(newListJson[0])