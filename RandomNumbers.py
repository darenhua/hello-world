import random
random.seed()

randomNumbers = []

def randNums(amount):
    for i in range(amount):
        randomNumbers.append(random.random())

randNums(50)
print(randomNumbers)
