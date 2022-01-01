# Using loops and decisions to iterate through collections and to test for conditions. 
# Can be used to search for desired values, identify values, extract values, etc. 

# COUNTER CONTROLLED LOOPS
# Iterate through the list and extract any outliers above 50.
# Place the number in a new list.
temps = [35, 22, 43, 88, 12, 57, 30]
threshhold = 50
outliers = []

count = 0
while count < len(temps):
    if temps[count] > threshhold:
        outliers.append(temps[count])
    count += 1

print("The following are the outliers from the temps list: ")
count = 0
while count < len(outliers):
    print("\t", outliers[count])
    count += 1



#Find and exctract words beginning with 'l', store in lWords list.
words = ["Aliqua", "nostrud", "labore", "enim", "lostrud", "ad", "aliquip", "voluptate", "ea", "qui", "exercitation", "leniam", "et", "laborum", "qui", "laboris"]
lWords = []
count = 0
print("Extracting words...")
while count < len(words):
    if(words[count][0].lower() == 'l'):
        lWords.append(words.pop(count))
    count += 1

count = 0
print("The following words have been collected:")
while count < len(lWords):
    print(lWords[count])
    count += 1


# SENTINEL_VALUE CONTROLLED LOOP
# Used to give the user control over when a loop ends by detecting
# a specific 'sentinel value', which triggers the loop to end. 
option = 1
numbers = []
option = input("Enter numbers or -1 to quit: ")
while option != "-1":
    numbers.append(option)
    option = input("Enter numbers or -1 to quit: ")

count = 0
while count < len(numbers):
    print(numbers[count])
    count += 1

