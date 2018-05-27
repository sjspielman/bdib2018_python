"""
The file fixed_width.txt is a *fixed-width* file, meaning that each column is delimited by an arbitrary number of spaces to increase human-readability. This format, however, is the bane of the programmer's existence, as we like to have standardized delimiters. Use regular expressions to convert this file into a CSV file called fixed_width_asCSV.csv.
"""

import re ## Load the re module 

## Read the original file, saving entire contents to a single string
with open("fixed_width.txt", "r") as f:
    contents_fixed = f.read()
    
## Use re.sub() to convert spaces to commas
contents_csv = re.sub(" +", ",", contents_fixed)

## Save to new file
with open("fixed_width_asCSV.csv", "w") as f:
    f.write(contents_csv)