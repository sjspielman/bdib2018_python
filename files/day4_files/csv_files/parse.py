import os


all_files = os.listdir("./")


with open("out.txt", "w") as f: 
    f.write("id,model,mle\n")
    for file in all_files:
        if file.startswith("ENSG"):
            outline = file.split(".")[0] + "," + file.split(".")[2] + ","
            
            with open(file, "r") as f2:
                thisline = f2.readlines()[-2]
            value = thisline.split(",")[1]
            outline += value + "\n"
            f.write(outline)
