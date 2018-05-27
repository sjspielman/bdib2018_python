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
	
	Incorporate the `sys` module to have these five (or four) *command line arguments*, in this order:
        + chromosome of interest
        + strand of interest
        + length of interest 
        + version of interest (if you took that step above!)
        + output file name

	Remember: `sys` always reads in arguments as strings, so you may need to convert to numbers with `int()` or `float()`.

FOR THIS SOLUTION, ALL OPTIONS ARE INCORPORATED **WITH SYS**. See corresponding file `part3_q2_withoutsys.py` for the alternative solution.


I ENCOURAGE YOU TO TEST OUT THIS SCRIPT WITH A VARIETY OF INPUT OPTIONS TO CONFIRM THE BEHAVIOR!!!!!!!
"""

import re
import sys
infile = "sacCer3_ncbiRefSeqCurated.gtf"

## we have 5 command line arguments ##
assert(len(sys.argv) == 6), "Incorrect arguments. \n\nCorrect usage: python3 part3_q2_withsys.py <chromosome> <strand> <length> <version> <output file name>"

chr = sys.argv[1].upper()
strand = sys.argv[2]
length = int(sys.argv[3])
version = sys.argv[4]
outfile = sys.argv[5]

feature = "CDS" ## defining for clarity

outfile_handle = open(outfile, "w") ## open for writing

with open(infile, "r") as gtf:

    for line in gtf:
        splitline = line.split("\t") ## create a list of columns for the given line
    
        
        ## Chromosome is column 0.
        if splitline[0].upper() != chr:
            continue
        
        ## Feature is column 2.
        if splitline[2].upper() != feature:
            continue
             
        ## Start and stop are columns 3 and 4. we want stop - start to be >=length
        ## the +1 is to include the starting index in the total length, which regular subtraction won't. this is a basic math thing.
        if int(splitline[4]) - int(splitline[3]) + 1 < length:
            continue
        
        ## Strand is column 6. We want a + symbol here
        if splitline[6] != strand:
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
            if find_version[0] == version:
                ## HUZZAH! IF WE HAVE MADE IT TO HERE, EVERY CONDITION WE WANT IS SATISFIED AND WE CAN SAVE THE LINE TO THE OUTPUT!!!
                outfile_handle.write(line)

## close up the output
outfile_handle.close()
                
                    
                
            
                
        
        
        
             
        