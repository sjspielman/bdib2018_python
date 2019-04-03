import sys


assert(len(sys.argv) == 6), "\n\nUsage: python3 parse_gtf.py <feature> <chr> <strand> <threshold> <version>"


feature_of_interest    = sys.argv[1].upper()
chromosome_of_interest = sys.argv[2].upper()
strand_of_interest     = sys.argv[3].upper()
threshold              = int(sys.argv[4])
version                = sys.argv[5]

print(feature_of_interest)


input_file = "sacCer3_ncbiRefSeqCurated.gtf"
output_file = "new.gtf"


with open(input_file, "r") as f:
    inlines = f.readlines()
    


with open(output_file, "w") as f:
    for line in inlines:
        split_line = line.strip().split("\t")
        
        c1 = split_line[2].upper() == feature_of_interest
        c2 = split_line[0].upper() == chromosome_of_interest
        c3 = split_line[6].upper() == strand_of_interest
        c4 = abs(int(split_line[4]) - int(split_line[3])) + 1 >= threshold
        
        
        ##method 1
        #c5 = '.1"' in split_line[-1]
        ##method 2
        c5 = split_line[-1].endswith('.' + version + '";')

        
        if c1 and c2 and c3 and c4 and c5:
            f.write(line)
        
    
    
        