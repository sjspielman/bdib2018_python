---
title: Introduction to Python, 2018 
author: Day 1 Exercises
documentclass: extarticle
fontsize: 12pt
geometry: margin=0.75in
---

## Part I: Working with numbers

Perform the following basic operations in Python:

+ Add two numbers
+ Multiply two numbers
+ Assign a number to a variable and then print the variable
+ Assign two numbers to two different variables, then assign the product of those two variables to a third.  
+ Print the third variable.



## Part II: If statements

1. Define a numeric variable, and use an `if/else` statement to determine if the number is greater than zero. Your code should print a sentence indicating if the number is greater than zero or not.

2. Modify the above `if/else` statement to write an `if/elif/else` statement to determine if the variable is greater than, less than, or equal to zero. Again, print a sentence indicating the number's value relative to zero.

3. Define *two* numeric variables, and use `if/elif/else` statement to determine which variable is larger (hint: they might be equal!). Again, print a sentence indicating which value is larger. This sentence should include both variable values.

4. Define a variable `animal = "python"`. This type of variable is a *string*, meaning it is made of characters and defined with quotation marks.  Write an `if/elif/else` statement to determine if the there are more than 10 letters in the variable `animal` (Hint: use the `len()` function!). Have your code print an informative message.

5. 	In Texas, you can be a member of the elite "top 1%" if you make at least $423,000 per year. Alternatively, in Hawaii, you can be a member once you start making at least $279,000 per year! Finally, if you live in New York, you need to earn at least $506,000 a year to make the cut. 
Andrew is CEO of Big Money Company, and he earns $425,000 per year, and Stacey is CEO of Gigantic Money Company with an annual salary of $700,000. Use a series of `if` statements to determine, and print, whether Andrew and Stacey would be considered top 1%-ers in Texas, Hawaii, and New York each. For this task, you should:

    * Define specific variables for the elite thresholds
    * Define specific variables for each person
	* Compare the variables to one another (as opposed to directly comparing numbers)
	 	

## Part III: Working with strings 

First, define the following variables:

``` python
	mammal  = "orangutan"
	bird    = "sparrow"
```
1. Print a statement that reads "My two variables have values orangutan and bird." Make sure to use your variables when printing (do not simply copy/paste this sentence).

2. Use indexing to print the **third** character in each of the two variables (hint: it's "a" for both!). Then, write an `if/else` statement to determine if the third letter is the same or different for these two variables. 

3. Use the method `.upper()` to *print* the variable `bird` as all uppercase. Then, modify this code to *redefine* the variable `bird` to be all uppercase. As always, print to confirm!

4. Use the method `.count()` to count how many `r`'s are in the variable `mammal`. Once you have this working, write an `if/elif/else` statement to check which variable has more `r`'s. Print informative statements accordingly.

5. Create a new variable called `both_animals` which contains the contents "SPARROWorangutan". Make sure to do this entirely with variable names (not with the actual words themselves!!). 



## Part IV: Working with lists 

First, define this list variable: `numbers = [0, 1, 1, 2, 3, 5, 8, 13]`.

1. Use indexing to print out the *fourth* item of the list. Now, use indexing to *redefine* the fourth element of the list `numbers` to be -10. Print the list to check.

2. Use the `.index()` method to determine which position in the list contains the value `5`, and redefine this value as `15`.

3. Use the `.count()` method to determine how many items in this list are equal to `1`. Use an `if` statement to print out whether this value is equal to 2 (the correct answer).

4. Use indexing to the print *last two* items of the list. Do this in two ways:

	1. Use the `len()` function to first determine the length of the list, and then print the last two items with this information
	2. Use negative indexing

5. Create a new variable called `original_length` which contains the length of the list `numbers` (use the function `len()`). Now perform the following tasks, being sure to print after each one!

	1. Use the method `.append()` to add the new entry `21` to the end of the list `numbers`. 
	2. Create another variable called `updated_length` which contains the length of `numbers` after you have appended 21. 
	3. Write an `if/else` statement to check if `updated_length` is one larger than `original_length`. Try to incorporate the operator `+=` into your code. Rememeber, you can build this up in stages (i.e. you don't need to start with `+=` in the first try!). 
 
6. Write an `if/elif/else` statement to compare the sum of the list to the value 50. Use the `sum()` function, which adds up all items in a list, for this task.

7. Create a new list: `numbers2 = [-4, -8, -12, -16]`, and *append* this new list to `numbers`. This code has created a *nested list*. Print the final length of the list "numbers". Did you expect this? Why or why not?

8. Finally, determine the length of the final entry in `numbers` using indexing and the `len()` function. 