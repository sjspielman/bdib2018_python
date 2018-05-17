# This python script contains solutions to Day One Python Exercises


####### Section 2.1: If statements #######

# Defining variables
a = -4.2
b = 55
animal = "python"

## 2.1.1 ##
compare = 100 # Define variable used for comparison *outside* of if statement to avoid hard-coding

#2.1.1 a-b
if a > compare:
    print("It is greater than", compare)
elif a < compare:
    print("It is less than", compare)
else:
    print("It is equal to", compare)

#2.1.1 c
if a > compare:
    dog = "beagle"
elif a < compare:
    dog = "spaniel"
else:
    dog = "labrador"
print(dog)


## 2.1.2 ##
if b % 2 == 0:
    print(b, "is even.")
elif b % 2 == 1:
    print(b, "is odd.")

## 2.1.3 ##
compare2 = 10

if len(animal) > compare2:
    print("The length of the word", animal, "is greater than", compare2)
else:
    print("The length of the word", animal, "is not greater than", compare2)
    
## 2.1.4 ##
Texas=423000
Hawaii=279000
NewYork=506000

Andrew=425000
Stacey=700000

# The code below can also be repeated for comparisons for Andrew instead of Stacey
if Stacey >= Texas:
    print("Stacey is a 1%er in Texas.")

if Stacey >= Hawaii:
    print("Stacey is a 1%er in Hawaii.")

if Stacey >= NewYork:
    print("Stacey is a 1%er in New York.")



    
    
    
    
    
    




