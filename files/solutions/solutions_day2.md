---
layout: page
permalink: /day2_solutions
---

# Day 2 Solutions

**Day 2 materials can be found [here]({{ '/day2' | relative_url }})**

----------------------------

## Part I: For loops


First, define the following two variables:
	
```python
numbers = [0, 1, 1, 2, 3, 5, 8, 13]
animals = ["gorilla", "canary", "frog", "moth", "nematode"]
```

1. Write a for-loop over the list `numbers`. At each iteration, print the value in `numbers` plus 2. 

    ```python
    for number in numbers:
    	print(number + 2)
    ```
    
2.  Write a for-loop over the list `animals`. At each iteration, print out the value in `animals` followed by its length. Your code should print out the following:

    ```python
    for animal in animals:
    	print(animal, len(animal)) 
    ```

3. Write a for-loop over the list `animals`. At each iteration, print out the uppercase version of each animal (do not redefine anything, just print!). Your code should print out the following:
       
    ```python
    for animal in animals:
    	print(animal.upper())
    ```
 
4. Write a new for-loop to create a new list called `upper_animals` which should contain the uppercase versions of all items in `animals`. Hint: For this task, you will need to define the list `upper_animals` *before* entering the for-loop, and you will need to use the method `.append()` to build up this list as you go. Print the final list after the for-loop.
  
    ```python
    upper_animals = []
    for animal in animals:
    	upper_animals.append( animal.upper() )
	print(upper_animals)
    ```
    
5. Write a for-loop to create a new list called `negative_numbers` which should contain the negative values of the items in `numbers`, following a similar procedure to the previous task. Once this list is complete, write an `if/else` statement to check if the sum (hint: use the function `sum()`) of `negative_numbers` equals -1 times the sum of `numbers`.

	```python
	negative_numbers = []
	for number in numbers:
		negative_numbers.append(number * -1)
	
	numsum = sum(numbers)
	if sum(negative_numbers) == -1*numsum:
		print("correct")
	else:
		print("incorrect")
	```


6. Write a for-loop, using the `range()` function, to create a list of the powers of 2 from 2$^0$ to 2$^{15}$. (Note that in Python, the exponent symbol is `**`, as in `3**2 = 9`).

	```python
	## Loop to 16 since we want to *include* 15
	powers = []
	for i in range(16):
		powers.append(2**i)
	```

7. Modify the previous for-loop to create a list of *every other* power of 2 (specifically the even exponents) by modifying the arguments given to `range()`.

	```python
	even_powers = []
	for i in range(0, 16, 2):
		even_powers.append(2**i)
	```


## Part II: Dictionaries

1. Define this dictionary and perform the following tasks: 
	
	```python
	molecules = {"DNA":"nucleotides", "protein":"amino-acids", "hair":"keratin"}
    ```
    
	+ Add the key:value pair `"ribosomes":"RNA"` to the `molecules` and print to confirm.
	
		```python
		molecules["ribosomes"] = "RNA"
		```
	
	+ Add another key:value pair, `"ribosomes":"rRNA"` to the `molecules` dictionary and print. Do you understand why the dictionary contains the key:value pairs shown?
	
		```python
		molecules["ribosomes"] = "rRNA"
		
		## At this point, the key/value ribosomes:RNA will have been replaced with above.
		```
	
	+ Write a for-loop over the dictionary to print each key-value pair in sentence form, "<key> is comprised of <value>." (i.e., "DNA is comprised of nucleotides").
	
		```python
		for key in molecules:
			print(key, "is comprised of", molecules[key])
			
		## One alternative approach:
		
		for key, value in molecules.items():
			print(key, "is comprised of", value)
		```
	
	+ Write a for-loop over the dictionary to make a list of keys which are more than 5 letters long. For this task, you should employ an `if` statement, the `len()` function, and the `.append()` method. Print the list once it is made.
	
		```python
		length = 5
		longkeys = []
		for key in molecules:
			if len(key) >= length:
				longkeys.append(key)
		```
	
	+ Write a for-loop over the dictionary to make a list of *values* which contain the letter `a`. Perform this task in two ways:
	
		+ Use the `.count()` method to count the number of `a`'s in each dictionary value, and use an `if` statement to determine if `a`'s were found

		+ Use the `in` statement.

		```python
		## Using .count()
		letter = "a"
		a_values = []
		for key in molecules:
			num_a = molecules[key].count("a")
			if num_a > 0:
				a_values.append(molecules[key]) 

		## Using in
		letter = "a"
		a_values = []
		for key in molecules:
			if "a" in molecules[key]:
				a_values.append(molecules[key]) 
		```	

2. Congratulations, you've been hired as a zoo-keeper! Now you have to feed the animals. You received these handy Python dictionaries which tells you (a) to which category each animal belongs, and (b) what to feed each animal category. Perform the following tasks with these dictionaries:

    ```python	
	category = {"lion": "carnivore", 
		        "gazelle": "herbivore", 
		        "anteater": "insectivore", 
		        "alligator": "homovore", 
		        "hedgehog": "insectivore", 
		        "cow": "herbivore", 
		        "tiger": "carnivore", 
		        "orangutan": "frugivore"}
		 
	feed = {"carnivore": "meat", 
		    "herbivore": "grass", 
		    "frugivore": "mangos", 
		    "homovore": "visitors", 
		    "insectivore": "termites"}
	```
		  
	+ Determine what you should feed the orangutan and print the result.
	
		```python
		target_animal = "orangutan"
		print( feed[ category[target_animal] ])
		```
	
	+ Write a for-loop to loop over "feed" and print out what food each *-vore* eats. You might find it helpful to first loop over the "feed" dictionary and simply print the loop variable. Extend the code from there to print the full sentence.
		
	    ```python
	    for key in feed:
	    	print("The", key, "eats", feed[key])
	    ```

	+ Write a for-loop to print out what each *animal* eats. For this task, you should loop over the dictionary `category` and use indexing to obtain the relevant information from the `feed` dictionary to create your sentence. Your code should ultimately print the following (in arbitrary order):
	       
	       
	    ```python
	    for animal in category:
	    	itsfood = feed[ category[animal] ]
	    	print("The", animal, "eats", itsfood)
	    ```

	+ Modify the previous for-loop so that it creates a new dictionary called `animals_eat`. This dictionary should contain the exact animal:food pairs, e.g. `"lion": "meat"` will be one key:value pair. Print out the resulting dictionary.
	
		 ```python
		 animals_eat = {}		 
	    for animal in category:
	    	itsfood = feed[ category[animal] ]
	    	animals_eat[animal] = itsfood
	    print(animals_eat)
	    ```


## Part III: Practice our skills

1. A professor has decided to curve grades in a very special way, and you have been tasked with crunching the numbers. Here are the curving rules:

	+ Grades **above 95** are reduced by 10%
	+ Grades **between 75-95 (inclusive)** remain the same
	+ Grades **below 75** are raised by 10%. 

    Perform the following tasks:	
    <br>
	
	+ Create a list of new grades that reflects these rules from the following original grades:
	
        ```python
        grades = [45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58]
        
        ######################################################################
        
        upper_bound = 95
        lower_bound = 75
        rounding = 0.1
                
        new_grades = []
        for grade in grades:
        	if grade > upper_bound:
        		new_grades.append(grade * (1 - rounding))
        	elif grade <= upper_bound and grade >= lower_bound:
        		new_grades.append(grade)
        	elif grade < lower_bound:
        		new_grades.append(grade * (1+rounding))
	    ```

	+ The professor has changed his mind: he now wants to use a scaling factor of `0.078325` (instead of 0.1), because why not! Recompute the grades using this new scaling. **No hard-coding!**

	
        ```python
        grades = [45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58]
        
        ######################################################################
        
        upper_bound = 95
        lower_bound = 75
        rounding = 0.078325
                
        new_grades = []
        for grade in grades:
        	if grade > upper_bound:
        		new_grades.append(grade * (1 - rounding))
        	elif grade <= upper_bound and grade >= lower_bound:
        		new_grades.append(grade)
        	elif grade < lower_bound:
        		new_grades.append(grade * (1 + rounding))
	    ```

	+ The *nested* list below contains three sets of grades for silly professor's three classes. Create a new nested list with the curved grades for each of these groups. Hint: you will need to be appending new lists to lists!
	    
	    ```python
		all_grades = [[45, 94, 25, 68, 88, 95, 72, 79, 91, 82, 53, 66, 58], 
		    		    [23, 46, 17, 67, 55, 42, 31, 73], 
					  [91, 83, 79, 76, 82, 91, 95, 77, 82, 77]]
					  
		###############################################################
		
		new_grades = []
		for grade_list in all_grades:
			new_list = []
			for grade in grade_list:
	        	if grade > upper_bound:
	        		new_list.append(grade * (1 - rounding))
	        	elif grade <= upper_bound and grade >= lower_bound:
	        		new_list.append(grade)
	        	elif grade < lower_bound:
	        		new_list.append(grade * (1 + rounding))
				new_grades.append(new_list)
	    ```

	 + Now, imagine that those three sets of grades correspond, in order, to the classes indicated in this list:

        ```python
		class_names = ["Psychology 101", "Sociology 101", "Political Science 101"]
		```				  
		
		Create a *dictionary* representing the *curved* grades for each of these classes. Your final dictionary should have the class name as keys, and each list of curved grades as values. Hint: You will either need to use a *counter* variable in your loop, or loop over the grade list with `range(len(...))`.
		
		```	python
		
		### One solution
		new_grades = {} 
		for i in range(len(all_grades)):
			new_list = []
			for grade in all_grades[i]:
	        	if grade > upper_bound:
	        		new_list.append(grade * (1 - rounding))
	        	elif grade <= upper_bound and grade >= lower_bound:
	        		new_list.append(grade)
	        	elif grade < lower_bound:
	        		new_list.append(grade * (1 + rounding))
	        		
				## save this list with corresponding class name, indexed with `i`
				new_grades[ class_names[i] ] = new_list
		
		### Another solution
		new_grades = {} 
		i = 0
		for grade_list all_grades:
			new_list = []
			for grade in grade_list:
	        	if grade > upper_bound:
	        		new_list.append(grade * (1 - rounding))
	        	elif grade <= upper_bound and grade >= lower_bound:
	        		new_list.append(grade)
	        	elif grade < lower_bound:
	        		new_list.append(grade * (1 + rounding))
	        		
				## save this list with corresponding class name, indexed with `i`
				new_grades[ class_names[i] ] = new_list
			i += 1
	    ```


2. For this set of questions, you will calculate the molecular weight of a protein sequence, using this dictionary:

	```python	
	amino_weights = {"A":89.09, "R":174.20, "N":132.12, 
					"D":133.10, "C":121.15, "Q":146.15, 
					"E":147.13, "G":75.07, "H":155.16, 
					"I":131.17, "L":131.17, "K":146.19, 
					"M":149.21, "F":165.19, "P":115.13, 
					"S":105.09, "T":119.12, "W":204.23, 
					"Y":181.19, "V":117.15} 
    ```
	+ Calculate the molecular weight of this sequence: `"GAHYADPLVKMPWRTHC"`
		
		```python
		sequence = "GAHYADPLVKMPWRTHC"
		weight = 0.
		for aa in sequence:
			weight += amino_weights[aa]
		print(weight)
		```
	
	+ Now, calculate the molecular weight of this sequence *which contains ambiguities*: `"KLSJXXFOWXNNCPRHGGYA"`. Assume that the molecular weight of an ambiguous amino acid is the *average* weight of all amino acids.

		```python
		sequence = "KLSJXXFOWXNNCPRHGGYA"
		weight = 0.
		average_weight = sum( list(amino_weights.values()) ) / len(amino_weights)
		for aa in sequence:
			## standard amino acids that are in the dictionary
			if aa in amino_weights:
				weight += amino_weights[aa]
			else:
				weight += average_weight
		print(weight)
		```
		
3. For this question, you will count the number of each nucleotide in a DNA sequence. 

	+ Create a dictionary which contains key:value pairs as nucleotide:count for this sequence: `"ACATAGACCAGAGACT"`. Use the `.count()` method by looping over a list of nucleotides (`nucs = ["A", "C", "G", "T"]`) to solve this question.
	
		```python
		nucs = ["A", "C", "G", "T"]
		
		sequence = "ACATAGACCAGAGACT"
		nuc_counts = {}
		
		for nuc in nucs:
			nuc_counts[nuc] = sequence.count(nuc)
		print(nuc_counts)
		```
	
	
	+ Now, create a similar dictionary for this DNA sequence which contains *ambiguities*: `"AGCTANTAGNNNNNAGGATCCNNAANNNNCATAGC"`. This time, use a for-loop *over the sequence itself* to "build up" a dictionary of counts for those characters which appear in the sequence. 
	
		```python
		nucs = ["A", "C", "G", "T"]
		
		sequence = "AGCTANTAGNNNNNAGGATCCNNAANNNNCATAGC"
		nuc_counts = {}
		
		for nuc in sequence:
			if nuc in nuc_counts:
				nuc_counts[nuc] += 1
			else:
				nuc_counts[nuc] = 1		
		print(nuc_counts)
		```		
		
	+ Modify the previous code to make a dictionary of *percentages* of nucleotides, rather than counts.
	
		```python
		nucs = ["A", "C", "G", "T"]
		
		sequence = "AGCTANTAGNNNNNAGGATCCNNAANNNNCATAGC"
		denominator = len(sequence)
		nuc_counts = {}
		
		for nuc in sequence:
			if nuc in nuc_counts:
				nuc_counts[nuc] += 1/denominator
			else:
				nuc_counts[nuc] = 1/denominator
		print(nuc_counts)
		
		## Note: alternatively, you could make a dictionary of counts, and then write a second for-loop to divide the total counts. However, mathematically the approaches are equivalent and the approach presented here is more efficient. At the end of the day, though, either way will work great!
		```		