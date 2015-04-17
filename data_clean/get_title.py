from nltk.tokenize.stanford import StanfordTokenizer
from bs4 import BeautifulSoup
import nltk
import csv
import pdb
import time

filein = "/Users/apple/Downloads/Train/Train.csv"
fileout = "./title.txt"
fout = open(fileout, 'wb')
count = 0
codecount = 0
title_list = ""

with open(filein, 'rb') as csvfile:
    #reader_obj = csv.reader(csvfile, delimiter=',', quotechar='"')
    start = time.time()
    reader_obj = csv.reader(csvfile)
    for row in reader_obj:
    	# row[0] -> id
    	# row[1] -> title
    	# row[2] -> content
    	# row[3] -> tags
    	#soup = BeautifulSoup(row[2])
        #if soup.code != None:
        #    codecount += 1
        title_list += " " + row[1]
        check = int(time.time() - start) 
        if check >= 10:  
            print count, time.time() - start, "seconds" 
            start = time.time() 
        if not count%10000:
            word_list = StanfordTokenizer(path_to_jar="/Users/apple/Downloads//stanford-postagger-2015-01-29/stanford-postagger-2015-01-30/stanford-postagger.jar"\
                    ).tokenize(title_list)
            fout.write(' '.join(word_list).encode('utf-8') + "\n")
            title_list = ""
            print(count)
            #word_list = nltk.word_tokenize(row[1].encode('utf-8'))
        #if not codecount%10000:
        #    print codecount
        count += 1
    	#print(soup.get_text())
        #pdb.set_trace()

word_list = StanfordTokenizer(path_to_jar="/Users/apple/Downloads//stanford-postagger-2015-01-29/stanford-postagger-2015-01-30/stanford-postagger.jar"\
        ).tokenize(title_list)
fout.write(' '.join(word_list).encode('utf-8') + "\n")
title_list = []
print(count)
