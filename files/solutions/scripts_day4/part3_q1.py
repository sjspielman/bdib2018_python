"""
Download today's exercise files, and create a new Python script in the directory called `csv_files/`. This directory contains *real research data* from Stephanie's github. Files are named as:`<Ensembl-gene-id>.fna.<MODEL>.csv`, where each Ensembl gene ID has two associated model CSVs, called `JTT` and `WAG`. 

	For this exercise, write a script to process these files in order to create a *single new tab-separated file* with the following columns:
	    + `Ensembl-gene-ID`, obtained from the file name
	    + `Model`, obtained from the file name
	    + `MLE`, obtained from the file contents. This column should the value in each file's `MLE` column that is associated with the **second to last site** in each file (it will be different for each gene!)

	This task will require you to obtain information both from each file name, as well as from within each file. Use the `os` module to obtain all file names as part of this exercise, and any string methods that are appropriate.
"""

import os


path_to_csv_files = "csv_files/" ## If you are writing this script in the csv_files directory, make this string "./", which is a shortcut meaning "this directory"

## Get all the files of interest
files = os.listdir(path_to_csv_files)

output_file = "all_information.csv" # arbitrary name..

## For this example, I will keep the file for writing open the whole time and write to it while we loop over the input file
output_handle = open(output_file, "w")


## first we write our output header
output_handle.write("Ensembl-gene-ID,Model,MLE\n")

for file in files:
    ## make sure it's an acceptable file. sometimes computers litter secret files in places which will appear in os.listdir(), and we want only the csv files in the directory
    if file.endswith(".csv"):
    
        ## First, grab information from the file name itself
        split_filename = file.split(".") ### --> [ensembl id, "fna", model, "csv"]
        ensembl_gene_id = split_filename[0]
        model = split_filename[2]
        
        ## Now, open the file to obtain the MLE column from second to last site!
        ## MLE is the first column index (second actual column)
        with open(path_to_csv_files + file, "r") as f:
            lines = f.readlines()
        ## The next line is *extra* pythonic! We string together the following:
        ### negative indexing gives us 2nd to last line
        ### split that line on a comma
        ### select the 2nd column (index 1) to end up with the value we want
        mle = lines[-2].split(",")[1]
        
        ## instead of joining together with comma, we can also add the output together 
        output_handle.write(ensembl_gene_id + "," + model + "," + mle + "\n")
        

# finally, close the output file handle
output_handle.close()
        
        









