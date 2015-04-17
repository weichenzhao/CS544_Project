import os
import pdb
import json
import time
import random

input_name = "/Users/apple/Desktop/USC/CS544 NLP/project/data/"
output_name = "2m_dataset.txt"
standard = 1000 * 2000.0

# get the 2000 tags
tag_file = open('tag_2000.txt', 'r')
file_count = {}
for tag in tag_file:
    file_count[tag[:-1]] = 0
#print file_count

# get filename in input dir
files = list(os.listdir(input_name))
random.shuffle(files)
    
"""
    get 1000 file for each tag
    data_set format: 
        { tag : { 'id': file entry } }
"""
data_set = {}
chosen_id = {}
tot_count = 0
file_cnt = 0
round_ = 0

for data_file in files:
    file_cnt += 1
    print "processing", data_file, file_cnt
    fin = open(input_name + data_file, 'r')
    data_dict = json.load(fin)
    fin.close()
    for key in data_dict.keys():
        if key not in chosen_id:
            # 0-title, 1-body, 2-code, 3-tags
            """
                popular tags tends to appear at first, if put these files
                into the tag dict, then it is possible that less frequent
                tags are ignored and therefore those tags might not get
                enough file. Reverse the order might do the work
            """
            tags = data_dict[key][3].split()
            tags.reverse()
            tag_list = []
            """
                have to consider all tags, and select the one currently have
                the least number of file append into the dataset
            """
            for t in tags:
                if t in file_count:
                    tag_list.append([file_count[t], t])

            if not tag_list == []:
                tag_list.sort()
                tot_count += 1
                t = tag_list[0][1]
                file_count[t] += 1
                # have this tag in data set, add into file dict of this tag
                if t not in data_set:
                    data_set[t] = {}
                data_set[t][key] = data_dict[key]
                # remove when got 1000 file for that key
                if file_count[t] >= 1000:
                    file_count.pop(t)
                if ( not tot_count % 10000 ) and tot_count > 0:
                    print "progress: ", tot_count * 100 /standard, "%", tot_count
                # already count this doc once. should not count it any more
                chosen_id[key] = True

    if len(file_count) == 0:
        break

print(len(data_set))
print(tot_count)
detail = open('dataset.detail.txt', 'w')
for key in data_set.keys():
    detail.write("key:" + key + " " + str(len(data_set[key].keys())))
    if len(data_set[key].keys()) < 1000:
        print len(data_set[key].keys())
#pdb.set_trace()
start = time.time()
json.dump(data_set, open(output_name, 'w'))
print "writting data used", time.time() - start, "seconds"
