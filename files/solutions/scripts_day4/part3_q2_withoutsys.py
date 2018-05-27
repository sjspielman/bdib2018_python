"""
Also in today's exercise files is a file called sacCer3_ncbiRefSeqCurated.gtf This file is a Gene Transfer Format (`gtf`) file obtained from the UCSC Genome Table Browser, and it is a standard file format in next-generation sequence analysis. It is a tab-delimited and contains gene information from *S. cerevisiae*, with the following columns (but there is no header, as the format is standard):

	+ The chromosome
	+ The source of the information (in this case, all sources are the same)
	+ The type of sequence, also known as feature, in this case either `start_codon`, `CDS` (coding sequence), `exon`, `stop_codon`
	+ The starting index for the genomic feature
	+ The ending index for for the genomic feature
	+ The score for the feature (in this case all scores are `0.000000`)
	+ The strand of the feature, either `+` for positive or `-` for negative
	+ The phase of the feature, either `.`, `0`, `1`, or `2`. This information indicates the reading frame, specifically the number of bases that need to be skipped before the codon structure begins. A value of `.` indicates that there is no specific phase information to deal with
	+ The gene information with a specific idenfitier, in this case `gene_id`.
	
Write a script to...
    + Extract only lines whose feature is `CDS`, creating a new file called `sacCer3_ncbiRefSeqCurated_EXON.gtf`. Perform this task by specifically asking (using `if`) if the third column is equal to "CDS".
	+ Modify the previous script to again create a new file only of CDS's, but this time do so for *only* sequences which fall on chromosome `chrV`.
	+ Modify yet again to export exons from chrV, with the additional condition that you should only consider CDS's on the *positive* strand
	+ Modify yet again, with the additional condition that you should only consider CDS's which are $$\geq500$$ base pairs in length.
	+ Modify yet again, considering only CDS's whose gene_id is the **first** version of the gene. More specifically, gene ids are named as `NM_<somenumbers>.<VERSIONUMBER`. In other words, you want the number after the decimal to equal 1.

FOR THIS SOLUTION, ALL OPTIONS ARE INCORPORATED **WITHOUT SYS**. See corresponding file `part3_q2_withsys.py` for the alternative solution.
"""

import re

infile = "sacCer3_ncbiRefSeqCurated.gtf"
outfile = "sacCer3_ncbiRefSeqCurated_MODIFIED.gtf"

## GTF files can be very large, so it's best not to fully read them into memory. Here, we loop over the lines while the file is open
## We also open the output file from the get-go, and write to it while looping over the input file - remembering to close at the end!!

outfile_handle = open(outfile, "w") ## open for writing

with open(infile, "r") as gtf:

    for line in gtf:
        splitline = line.split("\t") ## create a list of columns for the given line
        
        ##### Here, I'm going to check for each desired condition. IF ONE IS NOT MET, I will use the *continue* command to simply move on to the for-loop iteration, bringing us to test out the next line to see if we should save it.
        #### I'm also converting all strings, **just for the if statements but not saved** to uppercase just to be extra sure that the string I'm comparing it to (eg CDS) will match the case of the file.
        
        ## Chromosome is column 0. We want chrV
        if splitline[0].upper() != "CHRV":
            continue
        
        ## Feature is column 2. We want CDS
        if splitline[2].upper() != "CDS":
            continue
             
        ## Start and stop are columns 3 and 4. we want stop - start to be >=500
        ## the +1 is to include the starting index in the total length, which regular subtraction won't. this is a basic math thing.
        if int(splitline[4]) - int(splitline[3]) + 1 < 500:
            continue
        
        ## Strand is column 6. We want a + symbol here
        if splitline[6] != "+":
            continue
        
        ## Gene id is column 8 (last column). we want only the first version
        #### a bit more is required for this column. we'll need to use regular expressions to get the version out
        #### for example, a column might be:  gene_id "NM_001178157.1";   
        #### we need the ".1" part to equal .1
        find_version = re.findall("\w\w_\d+\.(\d)", splitline[8]) ## capturing with re.findall produces a list of captures
        ## we are expecting a single match. if we found 0 or more than 1 matches, something isn't quite right. so we should probably skip the line entirely since version cannot be determined
        if len(find_version) != 1: 
            continue
        else:
            if find_version[0] == "1":
                ## HUZZAH! IF WE HAVE MADE IT TO HERE, EVERY CONDITION WE WANT IS SATISFIED AND WE CAN SAVE THE LINE TO THE OUTPUT!!!
                outfile_handle.write(line)

## close up the output
outfile_handle.close()
                
                    
                
            
                
        
        
        
             
        