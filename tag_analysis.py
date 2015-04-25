import os
import pdb
import sys
import json
import time
import random

input_name = "/Users/apple/Desktop/USC/CS544 NLP/project/data/"

tot = 0 # tot number of questions
count = 0 # tot number of tags
max_tag = 0

# get filename in input dir
files = list(os.listdir(input_name))
random.shuffle(files)

file_cnt = 0
for data_file in files:
    if not data_file[0] == 's':
        continue

    file_cnt += 1
    print "processing", data_file, file_cnt
    fin = open(input_name + data_file, 'r')
    data_dict = json.load(fin)
    fin.close()
    print "load finished"
    for index in data_dict:
        tot += 1
        tags = len(data_dict[index][3].split())
        if tags > max_tag:
            max_tag = tags
        count += tags

        if tot % 1000 == 0:
            print tot, count, max_tag

start = time.time()
print "used", time.time() - start, "seconds"

import pdb
pdb.set_trace()
