import re

input_file = "fixed_width.txt"
output_file = "fixed_with_asCSV.csv"



# with open(input_file, "r") as f:
#     fixed_lines = f.readlines()
# with open(output_file, "w") as f:
#     for line in fixed_lines:
#         newline = re.sub(" +", ",", line)
#         f.write(newline)




with open(input_file, "r") as f:
    original = f.read()

new = re.sub(" +", "\t", original)
with open(output_file, "w") as f:
    f.write(new)

