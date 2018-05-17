# This python script contains solutions to Day Two Python Exercises

#### Section 1: Working with Lists and Strings ####

numbers = [0, 1, 1, 2, 3, 5, 8, 13]
mammal  = "orangutan"
bird    = "sparrow"

## 1.1
print(numbers[3])
numbers[3] = -10
print(numbers)


## 1.2
original_length = len(numbers)
numbers.append(21)
updated_length = len(numbers) 
print(original_length, updated_length)

if updated_length - 1 == original_length:
    print("append worked")
else:
    print("append failed")


## 1.3
numbers_sum = sum(numbers)
compare_sum = 50
if numbers_sum < compare_sum:
    print("The sum is less than", compare_sum)
else:
    print("The sum is not less than", compare_sum)
 
## 1.4
letter = "a"
mammal_a = mammal.count(letter)   
bird_a = mammal.count(letter)   
if mammal_a > bird_a:
    print("The word", mammal, "has more", letter, "'s than", bird)
elif mammal_a < bird_a:
    print("The word", bird, "has more", letter, "'s than", mammal)
else:
    print("The word", mammal, "has the same number of", letter, "'s as", bird)

## 1.5
bird = bird.upper()
print(bird)


## 1.6 
both_animals = bird.upper() + mammal
print(both_animals)
print( both_animals.count("o") )


## 1.7
numbers[0] = both_animals
print(numbers)

## 1.8
numbers2 = [-4, -8, -12, -16]
numbers[-1] = numbers2
print(len(numbers))

## 1.9
print( len(numbers[-1]) )




#### Section 2: For-loops ####

numbers = [0, 1, 1, 2, 3, 5, 8, 13]
animals = ["gorilla", "canary", "frog", "moth", "nematode"]

## 2.1
for x in numbers:
    print(x + 2)

## 2.2
for animal in animals:
    print(animal, len(animal))

## 2.3
for animal in animals:
    print(animal.upper())

## 2.4
cap_animals = []
for animal in animals:
    cap = animal.upper()
    cap_animals.append(cap)
print(cap_animals)

## 2.5
negative_numbers = []
for num in numbers:
    negative_numbers.append( -1 * num )
print(negative_numbers)

if sum(negative_numbers) == -1 * sum(numbers):
    print("The negative sum is correct!")
else:
    print("The negative sum is not correct.")    


## 2.6
for x in range(16):
    print(2**x)
    
## 2.7
for x in range(0, 16, 2):
    print(2**x)

for x in range(0, 16):
    if x%2 == 0:
        print(x**2)





#### Section 3: Working with dictionaries ####


## 3.1
molecules = {"DNA":"nucleotides", "protein":"amino acids", "hair":"keratin"}

molecules["ribosomes"] = "RNA"
print(molecules)

molecules["ribosomes"] = "rRNA"
print(molecules)


## 3.2
category = {"lion":  "carnivore", "gazelle":  "herbivore", "anteater": "insectivore", "alligator":  "homovore", "hedgehog":  "insectivore", "cow": "herbivore", "tiger":  "carnivore", "orangutan":  "frugivore"}
feed = {"carnivore":  "meat", "herbivore":  "grass", "frugivore":  "mangos", "homovore":  "visitors", "insectivore":  "termites"}

## 3.2a
cat = category["orangutan"]
print(feed[cat])

## 3.2b
for f in feed:
    print("The", f, "eats", feed[f])

## 3.2c
for cat in category:
    print("The", cat, "eats", feed[category[cat]])

## 3.2d
animals_eat = {}
for cat in category:
    animals_eat[cat] = feed[category[cat]]
print(animals_eat)
    















































