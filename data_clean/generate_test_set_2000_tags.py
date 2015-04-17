import os
import pdb
import json

input_name = "/Users/apple/Desktop/USC/CS544 NLP/project/data/"
output_name = "dataset.txt"
standard = 1000 * 2000.0

# get the 2000 tags
tag_file = open('tag_2000.txt', 'r')
file_count = {}
for tag in tag_file:
    file_count[tag[:-1]] = 0
#print file_count

# get filename in input dir
files = set(os.listdir(input_name))
    
"""
    get 1000 file for each tag
    data_set format: 
        { tag : { 'id': file entry } }
"""
data_set = {}
tot_count = 0
for data_file in files:
    print "processing", data_file
    fin = open(input_name + data_file, 'r')
    data_dict = json.load(fin)
    for key in data_dict.keys():
        # 0-title, 1-body, 2-code, 3-tags
        tags = data_dict[key][3].split()
        for t in tags:
            if t in file_count:
                tot_count += 1
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
    if len(file_count) == 0:
        break

print(len(data_set))
#pdb.set_trace()
json.dump(data_set, open(output_name, 'w'))
