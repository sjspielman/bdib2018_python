# This python script contains solutions to Day Three Python Exercises

#### Section 1: For loop and if/else ####

## 1.1
curve_percent = 0.1
upper_limit = 95
lower_limit = 75

# 1.1a
grades = [45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58]
new_grades = []
for grade in grades:
    if grade > upper_limit:
        new = grade * (1. - curve_percent)
    elif grade <= upper_limit and grade >= lower_limit:
        new = grade
    elif grade < lower_limit:
        new = grade * (1. + curve_percent)
    new_grades.append(new)
print(new_grades)

## 1.1b
curve_percent = 0.078325 
# Simply re-run the code from above, using this newly-defined curve_percent variable

## 1.1c
all_grades = [[45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58], [23, 46, 17, 67, 55, 42, 31, 73], [91, 83, 79, 76, 82, 91, 95, 77, 82, 77]]
new_class_grades = []

for class_grades in all_grades:
    section = []
    for grade in class_grades:
        if grade > upper_limit:
            new = grade * (1. - curve_percent)
        elif grade <= upper_limit and grade >= lower_limit:
            new = grade
        elif grade < lower_limit:
            new = grade * (1. + curve_percent)
        section.append(new)
    new_class_grades.append(section)

## 1.1d
class_names = ["Psychology 101", "Sociology 101", "Political Science 101"]
grades_dict = {}
for i in range(len(class_names)):
    name = class_names[i]
    curved_grades = new_class_grades[i]
    grades_dict[name] = curved_grades
print(grades_dict)



## 1.2
amino_weights = {"A":89.09, "R":174.20, "N":132.12, "D":133.10, "C":121.15, "Q":146.15, "E":147.13, "G":75.07, "H":155.16, "I":131.17, "L":131.17, "K":146.19, "M":149.21, "F":165.19, "P":115.13, "S":105.09, "T":119.12,"W":204.23, "Y":181.19, "V":117.15}

seq = "GAHYADPLVKMPWRTHC"
seq_weight = 0
for aa in seq:
    seq_weight += amino_weights[aa]
print(seq_weight)


seq2 = "KLSJXXFOWXNNCPR"
seq_weight2 = 0
mean_weight = sum(amino_weights.values()) / len(amino_weights)
for aa in seq:
    if aa in amino_weights:
        seq_weight2 += amino_weights[aa]
    else:
        seq_weight2 += mean_weight
print(seq_weight2)











    


        
