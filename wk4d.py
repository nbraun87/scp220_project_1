aListOfNumbers = [23, 65, 27, 9, 63, 66]

# Print list using FOR loop
for x in aListOfNumbers:
    print(x)
print()

# Also, print numbers on 1 line.
for x in aListOfNumbers:
    print(x, end=' ')
print()
print()

# Use the Range function to provide an 'iterable' for stepping through the loop.
for x in range(len(aListOfNumbers)):
    print(aListOfNumbers[x], end=" ")
print()
print()



aDictOfValues = {'Mon': 57,
                 'Tue': 46,
                 'Wed': 46,
                 'Thu': 52,
                 'Fri': 48,
                 'Sat': 54,
                 'Sun': 55}


# Print Dict using FOR loop.
for x in aDictOfValues:
    print(x, aDictOfValues[x], end=' ')
    print()
print()


# NESTED LOOPS


employees = [['nathan', 'IT Coordinator', 27.50],
             ['john', 'Marketing', 30.76],
             ['nancy', 'CFO', 35.23]]

for x in employees:
    for y in x:
        print(y, end=" ")
    print()
print()

aListOfDicts = [{'Mon': 57, 'Tue': 46, 'Wed': 46, 'Thu': 52, 'Fri': 48, 'Sat': 54, 'Sun': 55},
                {'Mon': 44, 'Tue': 43, 'Wed': 45, 'Thu': 56, 'Fri': 60, 'Sat': 62, 'Sun': 58},
                {'Mon': 56, 'Tue': 57, 'Wed': 43, 'Thu': 40, 'Fri': 39, 'Sat': 42, 'Sun': 44}]

for x in aListOfDicts:
    for y in x:
        print(y, ':', x[y], end="\t")
    print()
