### This python script contains solutions to Day Four Python Exercises


####### Section 1: File Input/Output #######

## 1.1
file_handle = open("file1.txt", "r")
file_contents = file_handle.read()
file_handle.close()
print(file_contents)

with open("file1.txt", "r") as file_handle:
    file_contents = file_handle.read()
print(file_contents)


## 1.2
with open("file1.txt", "r") as file_handle:
    file_lines = file_handle.readlines()
with open("upper_file1.txt", "w") as file_handle:
    for line in file_lines:
        file_handle.write(line.upper())


## 1.3
with open("upper_file1.txt", "a") as file_handle:
    file_handle.write("\nI just created this upper-case file!")


## 1.4
with open("upper_file1.txt", "r") as file_handle:
    for line in file_handle:
        print(line)


## 1.4
num_search = 5
letter_search = "E"
with open("upper_file1.txt", "r") as file_handle:
    for line in file_handle:
        if line.count(letter_search) >= num_search:
            print(line)


## 1.5
length_check = 25
for i in range(1,21):
    filename = "file" + str(i) + ".txt"
    file_handle = open(filename, "r")
    for line in file_handle:
        if len(line >= length_check):
            print(line)



## 1.6
category = {"lion": "carnivore", "gazelle": "herbivore", "anteater": "insectivore", "alligator": "homovore", "hedgehog": "insectivore", "cow": "herbivore", "tiger": "carnivore", "orangutan": "frugivore"}
feed = {"carnivore":  "meat", "herbivore":  "grass", "frugivore":  "mangos", "homovore":  "visitors", "insectivore":  "termites"}

outfile = "animal_food.txt"
out_handle = open(outfile, "w")
for entry in category:
    sentence = "The " + entry + " eats " + feed[category[entry]] + ".\n"
    out_handle.write(sentence)




####### Section 2: Defining Functions #######

## 2.1
def check_one_percenter(salary):
    Texas=423000
    Hawaii=279000
    NewYork=506000
    if salary >= Texas:
        print("This salary is a 1%er in Texas.")
    if Stacey >= Hawaii:
        print("This salary is a 1%er in Hawaii.")
    if Stacey >= NewYork:
        print("This salary is a 1%er in New York.")
# Run the function:
check_one_percenter(400000)


## 2.2
def calc_powers(x):
    powers = []
    for i in range(16):
        powers.append(x**i)
    return powers
# Run the function:
powers_list = calc_powers(3)



## 2.3
def calc_powers(base, low, high):
    powers = []
    for i in range(low, high + 1):
        powers.append(base**i)
    return powers
# Run the function:
powers_list = calc_powers(3, 0, 5)



## 2.4
def curve_grades(grade_list, upper_limit, lower_limit, curve_percent):
    for grade in grade_list:
        if grade > upper_limit:
            new = grade * (1. - curve_percent)
        elif grade <= upper_limit and grade >= lower_limit:
            new = grade
        elif grade < lower_limit:
            new = grade * (1. + curve_percent)
        new_grades.append(new)
    return new_grades
#Run the function:
test_grades = [100, 50, 75]
curve_grades(test_grades, 90, 70, 0.25)


## 2.5
def calc_peptide_weight(peptide):
    amino_weights = {"A":89.09, "R":174.20, "N":132.12, "D":133.10, "C":121.15, "Q":146.15, "E":147.13, "G":75.07, "H":155.16, "I":131.17, "L":131.17, "K":146.19, "M":149.21, "F":165.19, "P":115.13, "S":105.09, "T":119.12, "W":204.23, "Y":181.19, "V":117.15}
    mean_weight = sum(amino_weights.values()) / len(amino_weights)
    weight = 0.
    for amino_acid in peptide:
        if amino_acid in amino_weights:
            weight += amino_weights[amino_acid]
        else:
            weight += mean_weight
    return weight
# Run the function
calc_peptide_weight("AAX")



## 2.6
def count_f_in_file(filename):
    with open(filename, "r") as file_handle:
        contents = file_handle.read()
    # Make contents all lowercase to count all the f's in one line of code. This way we don't have to count upper and lower case f.
    contents = contents.lower()
    num_f = contents.count("f")
    return num_f


## 2.7
def count_char_in_file(filename, character):
    with open(filename, "r") as file_handle:
        contents = file_handle.read()
    character = character.lower()
    contents  = contents.lower()
    num_char = contents.count(character)
    return num_char
