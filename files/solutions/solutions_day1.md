---
layout: page
permalink: /day1_solutions
---

# Day 1 Solutions

**Day 1 materials can be found [here]({{ '/day1' | relative_url }})**


## Part II: If statements

1. Define a numeric variable, and use an `if/else` statement to determine if the number is greater than zero. Your code should print a sentence indicating if the number is greater than zero or not.

	```python
		x = 72
		compare_to = 0
		if x > compare_to:
			print(x, "is greater than", compare_to)
		else:
			print(x, "is not greater than", compare_to)
	```
	
2. Modify the above `if/else` statement to write an `if/elif/else` statement to determine if the variable is greater than, less than, or equal to zero. Again, print a sentence indicating the number's value relative to zero.

	```python
		x = 72
		compare_to = 0
		if x > compare_to:
			print(x, "is greater than", compare_to)
		elif x < compare_to:
			print(x, "is less than", compare_to)
		else:
			print(x, "is equal to", compare_to)
	
	```

3. Define *two* numeric variables, and use `if/elif/else` statement to determine which variable is larger (hint: they might be equal!). Again, print a sentence indicating which value is larger. This sentence should include both variable values.

	+ *The solution to this question is contained within #2 above.*


4. Define a variable `animal = "python"`. This type of variable is a *string*, meaning it is made of characters and defined with quotation marks.  Write an `if/elif/else` statement to determine if the there are more than 10 letters in the variable `animal` (Hint: use the `len()` function!). Have your code print an informative message.

	```python
		animal = "python"
		compare_to = 10
		if len(animal) > compare_to:
			print("length is greater than", compare_to)
		elif len(animal) < compare_to:
			print("length is less than", compare_to)
		else:
			print("length is equal to", compare_to)
	```


5. 	In Texas, you can be a member of the elite "top 1%" if you make at least $423,000 per year. Alternatively, in Hawaii, you can be a member once you start making at least $279,000 per year! Finally, if you live in New York, you need to earn at least $506,000 a year to make the cut. 
Andrew is CEO of Big Money Company, and he earns $425,000 per year, and Stacey is CEO of Gigantic Money Company with an annual salary of $700,000. Use a series of `if` statements to determine, and print, whether Andrew and Stacey would be considered top 1%-ers in Texas, Hawaii, and New York each. For this task, you should:

    * Define specific variables for the elite thresholds
    * Define specific variables for each person
	* Compare the variables to one another (as opposed to directly comparing numbers)
	 	

	```python
		### Define 1% limits
		texas = 423000
		hawaii = 279000
		newyork = 506000
		
		### Define salaries
		andrew = 425000
		stacey = 700000
	
		### Compare Andrew
		if andrew >= texas:
			print("Andrew is elite in Texas")
		if andrew >= hawaii:
			print("Andrew is elite in Hawaii")
		if andrew >= newyork:
			print("Andrew is elite in New York")
			
		### Compare Stacey
		if stacey >= texas:
			print("Stacey is elite in Texas")
		if stacey >= hawaii:
			print("Stacey is elite in Hawaii")
		if stacey >= newyork:
			print("Stacey is elite in New York")
			
	```

## Part III: Working with strings 

First, define the following variables:

``` python
	mammal  = "orangutan"
	bird    = "sparrow"
```

1. Print a statement that reads "My two variables have values orangutan and sparrow." Make sure to use your variables when printing (do not simply copy/paste this sentence).

	
	``` python
		print("My two variables have values", mammal, "and", bird)
	```
	
2. Use indexing to print the **third** character in each of the two variables (hint: it's "a" for both!). Then, write an `if/else` statement to determine if the third letter is the same or different for these two variables. 

	``` python
		third_bird = bird[2]
		third_mammal = mammal[2]
		
		if third_bird == third_mammal:
			print("It's the same")
		else:
			print("It's different")
	```


3. Use the method `.upper()` to *print* the variable `bird` as all uppercase. Then, modify this code to *redefine* the variable `bird` to be all uppercase. As always, print to confirm!

	``` python
		## Just print the uppercase
		print(bird.upper()	third_mammal = mammal[2]
		
		## Now redefine
		bird = bird.upper()
	```


4. Use the method `.count()` to count how many `r`'s are in the variable `mammal`. Once you have this working, write an `if/elif/else` statement to check which variable has more `r`'s. Print informative statements accordingly.

	``` python	
		mammal_r = mammal.count("r")
		bird_r   = bird.count("r")
		
		
		if mammal_r > bird_r:
			print("mammal has more")
		elif mammal_r < bird_r:
			print("bird has more")
		else:
			print("same number of r's")	
	```



5. Create a new variable called `both_animals` which contains the contents "SPARROWorangutan". Make sure to do this entirely with variable names (not with the actual words themselves!!). 

	```python
		
		both_animals = bird.upper() + mammal.lower()
	```


## Part IV: Working with lists 

First, define this list variable: `numbers = [0, 1, 1, 2, 3, 5, 8, 13]`.

1. Use indexing to print out the *fourth* item of the list. Now, use indexing to *redefine* the fourth element of the list `numbers` to be -10. Print the list to check.

	```python
		## 4th item = 3rd index!
		index_of_interest = 3 		
		
		## just print
		print(numbers[index_of_interest])
		
		## now redefine
		numbers[index_of_interest] = -10s
	```


2. Use the `.index()` method to determine which position in the list contains the value `5`, and redefine this value as `15`.

	```python
		which_position = numbers.index(5)
		
		## redefine
		numbers[which_position] = 15
		
		### Alternatively, all in one go:
		numbers[ numbers.index(5) ] = 15
	```


3. Use the `.count()` method to determine how many items in this list are equal to `1`. Use an `if` statement to print out whether this value is equal to 2 (the correct answer).

	```python
		num1 = numbers.count(1)
		correct = 2
	
		if num1 == correct:
			print("it's 2!")
		else:
			print("it's not 2")		
	```


4. Use indexing to the print *last two* items of the list. Do this in two ways:

	1. Use the `len()` function to first determine the length of the list, and then print the last two items with this information
	2. Use negative indexing


	```python
		### Solution using len()
		total_length = len(numbers)
		print(numbers[total_length-2 : total_length])
		
		### Solution with negative indexing
		print(numbers[-2:=
		num1 = numbers.count(1)
		correct = 2
	
		if num1 == correct:
			print("it's 2!")
		else:
			print("it's not 2")		
	```

5. Create a new variable called `original_length` which contains the length of the list `numbers` (use the function `len()`). Now perform the following tasks, being sure to print after each one!

	1. Use the method `.append()` to add the new entry `21` to the end of the list `numbers`. 
	2. Create another variable called `updated_length` which contains the length of `numbers` after you have appended 21. 
	3. Write an `if/else` statement to check if `updated_length` is one larger than `original_length`. Try to incorporate the operator `+=` into your code. Rememeber, you can build this up in stages (i.e. you don't need to start with `+=` in the first try!). 
	
	```python
		original_length = len(numbers)
		
		## Append 21
		numbers.append(21)
		
		## created updated_length
		updated_length = len(numbers)
		
		## compare
		original_length += 1 ## for comparing
		if original_length == updated_length:
			print("append huzzah!")
		else:
			print("append fail")
	```

 
6. Write an `if/elif/else` statement to compare the sum of the list to the value 50. Use the `sum()` function, which adds up all items in a list, for this task.

	```python
		numsum = sum(numbers)
		compare_to = 50
		
		if numsum > compare_to:
			print("greater than", compare_to)
		elif numsum < compare_to:
			print("less than", compare_to)
		else:
			print("equal to", compare_to)
	```
	
7. Create a new list: `numbers2 = [-4, -8, -12, -16]`, and *append* this new list to `numbers`. This code has created a *nested list*. Print the final length of the list "numbers". Did you expect this? Why or why not?

	```python
		numbers2 = [-4, -8, -12, -16]
		numbers.append(numbers2)
		
		print(len(numbers)) ## the appended list creates only 1 more item!
	```
	
8. Finally, determine the length of the final entry in `numbers` using indexing and the `len()` function. 

	```python
		print(len(numbers[-1]))	
	```