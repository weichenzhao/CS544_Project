import pdb
import json
import time
import random

start = time.time()
standard = 10000
data = open('dataset.txt', 'r')
data_dict = json.load(data)
print "loading data used", time.time() - start, "seconds"

new_data = {}
tot_count = 0
keys = data_dict.keys()

# select 6k file, evenly for each key
for key in keys:
    new_data[key] = {}
    for i in range(2):
        file_id = data_dict[key].keys()[0]
        new_data[key][file_id] = data_dict[key][file_id]
        data_dict[key].pop(file_id)
        tot_count += 1
        if ( not tot_count % 1000 ) and tot_count > 0 :
            print "progress: ", tot_count * 100 /standard, "%", tot_count

# select 4k file, randomly
while tot_count < standard:
    # select a key randomly 
    key = keys[random.randint(0,1999)]
    # select a random index based on key
    index = data_dict[key].keys()[random.randint(0, len(data_dict[key].keys()) - 1)]
    new_data[key][index] = data_dict[key][index]
    tot_count += 1
    data_dict[key].pop(index)
    if ( not tot_count % 1000 ) and tot_count > 0 :
        print "progress: ", tot_count * 100 /standard, "%", tot_count

print(len(new_data))
json.dump(new_data, open('10k_data.txt', 'w'))
#pdb.set_trace()
