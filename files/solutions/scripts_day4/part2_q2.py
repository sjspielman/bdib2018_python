"""
    Use the `re` module to change the file contents of the file data1_raw.txt to match the contents of the file data1_clean.txt.
"""

import re

### Required changes:
# 1. Replace all tabs and spaces with a comma
# 2. Change columns 2, 3, 4, 5, 8, 9 to have a single decimal
# 3. Change column 7 to have no decimals
# 4. Columns 1 and 6 stay the same

## I'm going to define a dictionary indicating what to do with each column. Then, when looping over the columns, I can refer back to this dictionary to figure out how to change the value. Again, remember there are many ways to solve this task, and this is only one approach!!
## Also, this could have easily been a list, where instead of keys with numbers we can use the *index* of each list item as the column indicator. This approach is a bit more explicit and therefore less prone to the coder introducing bugs!
changes = {1: None, 
           2: "single", 
           3: "single", 
           4: "single", 
           5: "single",
           6: None, 
           7: "nodecimal", 
           8: "single",
           9: "single"
           }

input_file = "data1_raw.txt"
output_file = "data1_raw_matchclean.txt"

with open(input_file, "r") as f:
    input_lines = f.readlines()  ## Read as list of lines

## Create an empty list of new lines to write to the output file, which will contained "cleaned" versions of `input_lines`
all_newlines = []
for i in range(len(input_lines)):
    
    ## Split line into individual using re to split on **spaces or tabs**
    ## Perform this directly on the stripped line, to remove trailing whitespace. This means no more enter at the end of the lines
    line_split = re.split("[\t ]", input_lines[i].strip())
    
    # don't muck with header line!
    if i == 0:
        newline = line_split
    else:  
        ## Loop over columns in this line and append each updated column to newline as we loop
        newline = [] 
        col_index = 1 ## keep track of column count, starting from 1 to be consistent with my `changes` dictionary
        for col in line_split:        
            # simply append the column if no changes are required
            if changes[col_index] is None:
                newline.append(col)
        
            # single decimal point
            elif changes[col_index] == "single":
                newcol = re.sub("(\d+\.\d)\d+", "\\1", col)
                newline.append(newcol)
        
            # remove decimal entirely
            elif changes[col_index] == "nodecimal":
                newcol = re.sub("(\d+)\.\d+", "\\1", col)        
                newline.append(newcol)
        
            col_index += 1
    
    ## Now, join together the newline list and append to all_newlines
    newline2 = ",".join( newline )
    all_newlines.append(newline2)
    

## Finally save to output! We will write to the output file by JOINING all_newlines with "\n"!
with open(output_file, "w") as f:
    f.write("\n".join(all_newlines))
    
        
        
        
        
        
        
        
        
        
        
        
