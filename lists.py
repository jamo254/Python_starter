numbers = [1, 3,4,5]
print(numbers)
print(len(numbers))
# Looping over lists
for number in numbers:
    if number == 5:
       print("Found number", number)
    else:
        print(number)

list_nested = [[1, 2, 2, 4], ["cat", "bird", "bat"]]
print(list_nested[0][1])
print(list_nested[1][0])

# Negative indexes
span = ["cat", "bird", "bat"]
print(span[-1] + span[-2])

# Slicing lists
sliced_list = span[0:2]
print(sliced_list)

# Living out some indices 
print(span[:2])
print(span[0:-1])

# List Concatenation and List Replication

# Removing Values from list using del
groups = ["cat", "bird", "bat"]
del groups[1]
print("Groups:", groups)

# Range
for i in range(6):
    print(i)

# Using loops with lists
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for item in range(len(supplies)):
    print("Index " + str(item) + " in  supplies is " + supplies[item])

# Using random.choice() and random.shuffle() functions with lists

import random
pets = ["cat", "Dog", "Rackoon", "Fish"]
choose = random.choice(pets)
print("Random choice", choose)

# Shuffle lists

people = ["Bobi", "Alexa", "Ali", "Siri", "Kabu"]
shuffled = random.shuffle(people)
print("Shuffled list", shuffled)

span = 42
span += 3
print(span, "")

# Finding a vlue in  a list using index() method
people = ["Bobi", "Alexa", "Alin", "Siri", "Kabu"]
print(people.index("Alin"))
# Using append() and inserts() methods
people.append("Mark") #Adds items at the end of the list
print(people)
#Insert adds items at any point
people.insert(1, "Akmedi")
print("Add at:", people)

# Mutabiliy of lists - cal remove, add and change
electronics = ['phones', 'computers', 'radio']