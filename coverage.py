import os
import pdb
import sys
import json
import time
import random

input_name = "/Users/apple/Desktop/USC/CS544 NLP/project/data/"
output_name = ""
#article_num = int(sys.argv[1])
#standard = 100 * article_num * 1.0

# get the tags
tag_file = open('tag_count.txt', 'r')
tag_list = []
for line in tag_file:
    tag = line.split()[1]
    tag_list.append(tag)
#print tag_list[:20]

tot = 0 # tot number of questions
count = [0] * len(tag_list) # coverage

# get filename in input dir
files = list(os.listdir(input_name))
random.shuffle(files)

file_cnt = 0
for data_file in files:
    file_cnt += 1
    print "processing", data_file, file_cnt
    fin = open(input_name + data_file, 'r')
    data_dict = json.load(fin)
    fin.close()
    print "load finished"
    for index in range(len(tag_list)):
        if index % 1000 == 0:
            print tot, len(data_dict)
        rm = []
        for qid in data_dict.keys():
            tag_l = data_dict[qid][3].split()
            if tag_list[index] in tag_l:
                count[index] += 1
                rm.append(qid)
        for qid in rm:
            tot += 1
            data_dict.pop(qid)
        if len(data_dict) == 0:
            break
    print tot

result = [0] * len(tag_list)
result[0] = count[0]
for index in range(len(tag_list))[1:]:
    result[index] = count[index] + result[index - 1]

f_o = open('file_coverage.txt', 'w')
for index in range(len(tag_list)):
    s = str(index) +" \tcount:" + str(count[index]) + "\t tot:" + str(result[index]) + \
        "\t coverage:" + str( result[index] * 100 / tot ) + "% \t" + tag_list[index] + "\n"
    f_o.write(s)


start = time.time()
print "writting data used", time.time() - start, "seconds"
