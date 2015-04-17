from bs4 import BeautifulSoup
import csv
import pdb
import json
import time
#import os
#import psutil

"""
    segment the dataset into 51 smaller segemnt
"""
filein = "/Users/apple/Downloads/Train/Train.csv"
fileout = "./seg/segment_"
bytecount = 0
segment = 0
data = {}
mb = 1024 * 1024.0
#start_mem = psutil.Process(os.getpid()).memory_info()[0]
curr_mem = 0
diff = -1

with open(filein, 'rb') as csvfile:
    start = time.time()
    csvfile.next()
    #reader_obj = csv.reader(csvfile, delimiter=',', quotechar='"')
    reader_obj = csv.reader(csvfile)
    #csvout = csv.writer(fout, delimiter=',', quotechar='"')
    for row in reader_obj:
    	# row[0] -> id
    	# row[1] -> title
    	# row[2] -> content
    	# row[3] -> tags
        #if soup.code != None:
        #    codecount += 1
        #pdb.set_trace()
        code = ""
        list_id = int(row[0])
    	soup = BeautifulSoup(row[2])
        if soup.code != None:
            code = soup.code.get_text()
            junk = [s.extract() for s in soup('code')]
        # id            title         body       code   tag
        data[list_id] = [row[1], soup.get_text(), code, row[3]]
        bytecount += 4 + len(data[list_id][0]) + len(data[list_id][1]) + \
                     len(data[list_id][2]) + len(data[list_id][3]) + 45
        check = int(time.time() - start)

        if check >= 10:
            print bytecount/mb, time.time() - start, "seconds"
            start = time.time()
        
        if bytecount > 100 * mb:
            fout = open(fileout + str(segment) + ".txt", 'wb')
            json.dump(data, fout)
            fout.close()
            #pdb.set_trace()
            segment += 1
            print "reached 100mb, getting next file", segment
            data = {}
            bytecount = 0
            #fout = open(fileout + str(segment) + ".txt", 'wb')
            #csvout = csv.writer(fout, delimiter=',', quotechar='"')
        #fout.write(row)
        #if not codecount%10000:
        #    print codecount
        #fout.write(row[3] + "\n")
    	#print(soup.get_text())
    fout = open(fileout + str(segment) + ".txt", 'wb')
    json.dump(data, fout)
    fout.close()

