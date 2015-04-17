from bs4 import BeautifulSoup
import csv
import pdb

filein = "/Users/apple/Downloads/Train/Train.csv"
fileout = "./tags.txt"
fout = open(fileout, 'wb')
count = 0
codecount = 0

"""
    count how many files in the dataset
"""
with open(filein, 'rb') as csvfile:
    #reader_obj = csv.reader(csvfile, delimiter=',', quotechar='"')
    reader_obj = csv.reader(csvfile)
    pdb.set_trace()
    for row in reader_obj:
    	# row[0] -> id
    	# row[1] -> title
    	# row[2] -> content
    	# row[3] -> tags
    	soup = BeautifulSoup(row[2])
        #if soup.code != None:
        #    codecount += 1
        #if not count%10000:
        #    print count
        #if not codecount%10000:
        #    print codecount
        count += 1
        #fout.write(row[3] + "\n")
    	#print(soup.get_text())

print count
