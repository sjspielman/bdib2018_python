## VERSION 1: draft for loops and check with print statements
# import csv
#
# file = 'hyphy_output_long.txt'
# 
# f = open(file,'rU')
# lines = f.readlines()
# f.close()
# 
# sites=[['site','dnds','logL','LRT','pval']]
# 
# for line in lines:
# 	if "Site" in line[0:6]:
# 		line = line.strip().split() # .strip() removes extra spacing characters, .split() makes a list splitting on any space
# 		site = line[1]
# 		dnds = line[4]
# 		logL = line[8]
# 		LRT = line[11]
# 		pval = line[14]
# 		sites.append([site,dnds,logL,LRT,pval])
# 		
# 
# with open('hyphy_dnds.csv','w') as f:
# 	filewriter=csv.writer(f)
# 	filewriter.writerows(sites)
	
	
## VERSION 2: turn draft into functions
# import csv
# def parse_hyphy(infile):
# 	# read hyphy output file
# 	f = open(infile,'rU')
# 	lines = f.readlines()
# 	f.close()
# 
# 	sites=[['site','dnds','logL','LRT','pval']]
# 
# 	for line in lines:
# 		if "Site" in line[0:6]:
# 			line = line.strip().split() # .strip() removes extra spacing characters, .split() makes a list splitting on any space
# 			site = line[1]
# 			dnds = line[4]
# 			logL = line[8]
# 			LRT = line[11]
# 			pval = line[14]
# 			sites.append([site,dnds,logL,LRT,pval])
# 	return sites
# 
# def write_sites(sites,outfile):
# 	with open(outfile,'w') as f:
# 		filewriter=csv.writer(f)
# 		filewriter.writerows(sites)
# 
# def main():
# 	infile = 'hyphy_output_long.txt'
# 	outfile = 'hyphy_dnds.csv'
# 	data = parse_hyphy(infile)
# 	write_sites(data,outfile)
# 
# main()

## VERSION 3: include ability to specify file from command line with `sys` module, add doc strings
# import csv
# import sys
# def parse_hyphy(infile):
# 	"""
# 	This function takes a hyphy output file and searches for lines that show dnds stats. It takes each of these lines
# 	and saves values for an output file. It returns a list of lists of these numbers.
# 	"""
# 	# read hyphy output file
# 	f = open(infile,'rU')
# 	lines = f.readlines()
# 	f.close()
# 
# 	sites=[['site','dnds','logL','LRT','pval']]
# 
# 	for line in lines:
# 		if "Site" in line[0:6]:
# 			line = line.strip().split() # .strip() removes extra spacing characters, .split() makes a list splitting on any space
# 			site = line[1]
# 			dnds = line[4]
# 			logL = line[8]
# 			LRT = line[11]
# 			pval = line[14]
# 			sites.append([site,dnds,logL,LRT,pval])
# 	return sites
# 
# def write_sites(sites,outfile):
# 	"""
# 	This function writes the data to a file.
# 	"""
# 	with open(outfile,'w') as f:
# 		filewriter=csv.writer(f)
# 		filewriter.writerows(sites)
# 
# def main():
# 	"""
# 	This function requires two arguments from the commandline: 1) the infile to be parsed and 2) the outfile name.
# 	"""
# 	infile = sys.argv[1]
# 	print "infile is %s" %infile
# 	outfile = sys.argv[2]
# 	print "outfile is %s" %outfile
# 	data = parse_hyphy(infile)
# 	write_sites(data,outfile)
# 
# main()


## VERSION 4: use `re` module to locate specific lines and the `os` module to carry out parsing on a set of files
import csv
import sys
import re
import os

def find_files(directory, ending):
	"""
	This function takes two arguments, the directory and ending of files you want to parse. It returns a list of filenames that match these two descriptors.
	"""
	file_list = os.listdir(directory)
	files=[]
	for file in file_list:
		if file.endswith('long.txt'):
			files.append(file)
	return files

def parse_hyphy(files):
	"""
	This function takes a hyphy output file and searches for lines that show dnds stats. It takes each of these lines
	and saves values for an output file. It returns a list of lists of these numbers.
	"""
	# read hyphy output file
	sites=[['filename','site','dnds','logL','LRT','pval']]
	
	for file in files:
		f = open(file,'rU')
		lines = f.readlines()
		f.close()
		filename = file
		print "Now parsing 
		for line in lines:
			if re.search("^Site", line):
				line = line.strip().split() # .strip() removes extra spacing characters, .split() makes a list splitting on any space
				site = line[1]
				dnds = line[4]
				logL = line[8]
				LRT = line[11]
				pval = line[14]
				sites.append([filename,site,dnds,logL,LRT,pval])
	return sites

def write_sites(sites,outfile):
	"""
	This function writes the data to a file.
	"""
	with open(outfile,'w') as f:
		filewriter=csv.writer(f)
		filewriter.writerows(sites)

def main():
	"""
	This function requires  arguments from the command line: 
	1) the directory where infiles are located
	2) the common ending of all files of interest
	3) the name of the output file
	"""
	directory = sys.argv[1] # '.'
	ending = sys.argv[2]  # 'long.txt'
	outfile = sys.argv[3] # whateveryouwant.csv
	files = find_files(directory,ending)
	data = parse_hyphy(files)
	write_sites(data,outfile)

main()

