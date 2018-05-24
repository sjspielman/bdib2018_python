---
layout: page
permalink: /day3_solutions
---

# Day 3 Solutions

**Day 3 materials can be found [here]({{ '/day3' | relative_url }})**

----------------------------


## Part I: Functions

1. Write a function to compute the `GC` content of a DNA sequence. The function should accept a single argument, the DNA sequence, and return the GC *percentage*. Test your function with the nucleotide sequence `"AGCTATAGCATAGC"`.

	```python
	def calc_gc(sequence):
		num_gc = sequence.count("G") + sequence.count("C")
		percentage = num_gc / len(sequence)
		return percentage
	
	## Use function
	perc = calc_gc("AGCTATAGCATAGC")
	```

2. Write a function that calculates the percentage of a given nucleotide from a DNA sequence. The function should accept two arguments: the nucleotide of interest and the DNA sequence. It should return the nucleotide percentage. Test your function with the nucleotide sequence `"AGCTATAGCATAGC"`.

	```python
	def calc_nucleotide(sequence, nucleotide):
		return sequence.count(nucleotide) / len(sequence)
		
	## Use function, to count A's
	perc = calc_nucleotide("AGCTATAGCATAGC", "A")
	```


3. Write a function that calculates the percentage each nucleotide in a given DNA sequence. of a given nucleotide from a DNA sequence. The function should accept a single argument, the DNA sequence, and return *a dictionary* containing `key:value` pairs of `nucleotide:percentage`. You can assume that the provided sequence contains only A, C, G, T. Test your function with the nucleotide sequence `"AGCTATAGCATAGC"`.

	```python
	def calc_percentage(sequence):

    	total = len(sequence)
    	counts = {}
    	for nuc in sequence:
        if nuc not in counts:
            counts[nuc] = 1/total
        else:
            counts[nuc] +=1/total
    	return counts

	### Use function
	seq = "AGCTATAGCATAGC"
	value = calc_percentage(seq)
	```

4. Write a function to guess whether a provided sequence is DNA or protein. For this task, assume that any sequence comprised of $$\geq50$$% A, C, G, T is a DNA sequence. Test your function with the following two sequences:
	+ `"AGCTATGCATACGAGCATAGC"`
	+ `"AGIILLCPKLKKQWTATWCAGCATADSARCVLMKGC"`

	```python
	def is_it_protein(sequence):
		"""
			This information enclosed in a 3-quote block is a "docstring". It is the official place to document what the function does.
			
			This function returns `True` if the sequence is likely protein, and `False` if it is likely DNA.
		"""
    	nucleotides = "ACGT"
    	
    	## Determine percentage that are ACGT
    	nuc_perc = 0.
    	total_length = len(sequence)
    	for nuc in nucleotides:
    		nuc_perc += ( sequence.count(nuc)/ total_length )
    	
    	## Compare to 0.5
    	## Return true if mostly nucleotides, false otherwise
    	if nuc_perc >= 0.5:
    		return False
    	else:
    		return True

	### Use function
	seq1 = "AGCTATGCATACGAGCATAGC"
	is_it_protein(seq1)
	seq2 = "AGIILLCPKLKKQWTATWCAGCATADSARCVLMKGC"
	is_it_protein(seq2)
	```
	
	
5. Modify the previous function to *ignore all ambiguities in calculations*. Use this list of ambiguous characters for this task: `ambig = ["B", "J", "N", "O", "X", "Z"]`. Test your function with the following sequence:`"APAPPPKKLRATNNYPOPPBXXXXXNTYGCTATLMQASDFTDTCATAGC"`

	```python
	def is_it_protein(sequence):
		
		## First, we can remove all ambiguities from the sequence with .replace().
		## Then, we can make our protein/DNA guess based on the "clean" sequence.
		ambig = ["B", "J", "N", "O", "X", "Z"]
		for x in ambig:
			## loop to replace each amibuity with nothing (blank "")
			sequence = sequence.replace(x, "")
			    	nucleotides = "ACGT"
	    	
	    ## Determine percentage that are ACGT
	    nuc_perc = 0.
	    total_length = len(sequence)
	    for nuc in nucleotides:
	    	nuc_perc += ( sequence.count(nuc)/ total_length )
	    
	    ## Compare to 0.5
	    ## Return true if mostly nucleotides, false otherwise
	    if nuc_perc >= 0.5:
	    	return False
	    else:
	    	return True
	```

## Part II: File Input/Output

Files used in these exercises can be downloaded from the course website. Be sure to write your scripts in the same directory as these files!

1. Open the file `file1.txt` in read-mode, and print its contents to screen. Use the `.read()` method, which saves the contents of the file to a single string. Perform this task twice: once using `open` and `close`, and once using `with` control-flow.

	```python
	## Open and close
	f = open("file1.txt", "r")
	contents = f.read()
	f.close()
	print(contents)
	
	## with
	with open("file1.txt", "r") as f:
		f.read()
	print(contents)
	```
	
2. Open the file `file1.txt` in read-mode, and save all lines in this file to a list using the `.readlines()` method. Write a new file called `upper_file1.txt` which contains the same contents of `file1.txt` but in upper-case. Try to do this task using a single for-loop.

	```python	
	## open file for reading
	with open("file1.txt", "r") as f:
		filelines = f.readlines()
		
	## open new file to write (creates file on the fly!)
	with open("upper_file1.txt", "w") as f:
		## loop over filelines and write its uppercase version to the `f` handle
		for line in filelines:
			f.write(line.upper())
	```

	
3. Open the newly created file `upper_file1.txt` in read-mode. Loop over the file lines *without* using `.read()` or `.readlines()`, and print out lines as you loop.

	```python	
	with open("upper_file1.txt", "r") as f:
		for line in f:
			print(line)		
	```

4. Modify the previous for-loop to only print out lines in `upper_file1.txt` which contain at least (i.e. $$>=$$) 5 letter `E`'s. 
	
	```python	
	letter = "E"
	threshold = 5
	with open("upper_file1.txt", "r") as f:
		for line in f:
			if line.count(letter) >= threshold:
				print(line)		
	```
	
5. You should notice 20 files named `file1.txt, file2.txt, ..., file20.txt`. Write a for-loop to open each of these files (Hint: use the `range()` function to loop over file names). For each file, print each line that contains more than 25 characters.


	```python
	characters = 25
	for i in range(1, 21):  ## i will be 1-20 with this range() specification
		thisfile = "file" + str(i) + ".txt"
		with open(thisfile, "r") as f:
			## loop over lines, asking each time if it has > 25 characters and printing if true
			for line in f:
				if len(line) > characters:
					print(line)	
	```

6. Write another for-loop over the same 20 files. For each file, create a second file named `fileX_odd.txt` (where X=1-20) which contains only the *odd-numbered lines* from the original file. For this, use a *counter* in the for-loop that goes over file lines (this will count the line numbers), but be careful: Remember that python indexing starts from 0, but the first line is technically line #1! 

	```python
	for i in range(1, 21):  ## i will be 1-20 with this range() specification
	    thisfile = "file" + str(i) + ".txt"
	    savelines = []
	    with open(thisfile, "r") as f:
	        x = 1 ## start our counter variable at 1, so that it matches "human" line numbering!
	        for line in f:
	            if x%2 == 1: ## is i an odd number? if so, print!
	                savelines.append(line)
	            x += 1    # increment the counter for numbering the next line
	    
	    ## create and open output file for writing to
	    outfile = "file" + str(i) + "_odd.txt"
	    with open(outfile, "w") as f:
	        for line in savelines:
	            f.write(line)
	```



7. Convert our zoo-keeper dictionaries into a *comma-separated file* with the header `animal,vore,food`, and rows should contain corresponding information, i.e. `lion,carnivore,meat`. Perform this task with a *single* for-loop.
		
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
		    
	## Open output file for reading
	output_file = "animal_foods.csv"
	with open(output_file, "w") as f:
	
		## First, write header to file, including new line!
		f.write("animal,vore,food\n")	 
	    
	    ## now loop over dictionary to get vore and food lines per animal, writing to file as we go
	    for animal in category:
	    	vore = category[animal]
	    	itsfood = feed[ vore ]
	    	
	    	## line to write to file, including a newline symbols
	    	linetowrite = animal + "," + vore + "," + itsfood + "\n"
	    	
	    	## write the line to file
	    	f.write(linetowrite)
	```

8. Create a second zoo-keeper file by *converting* the CSV into a tab-separated file. Perform this task by reading in the CSV, *replacing* commas with tabs, where tabs can be created as the string `"\t"`. 

     ```python	
	infile = "animal_foods.csv"
	outfile = "animal_foods.txt" # note different extension
 
	with open(infile, "r") as f:
		first_contents = f.read()
	
	## replace all , with \t
	new_contents = first_contents.replace(",", "\t")
	
	## save to outfile
	with open(outfile, "w") as f:
		f.write(new_contents) 	 
	```	
