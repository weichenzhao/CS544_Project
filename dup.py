import json
import sys

f1 = open('500k_train.txt', 'r')
f2 = open('50k_test.txt', 'r')

dict_in1 = json.load(f1)
dict_in2 = json.load(f2)
print "load finished "

key_1 = dict_in1.keys()
key_2 = dict_in2.keys()
dic = {}
for tag in key_2:
    dic[tag] = 0

tot_1 = len(dict_in1)
tot_2 = len(dict_in2)

#tmp = [val for val in key_1 if val in key_2]
print "compairing"
num = 0
dup = []
for val in key_1:
    num += 1
    if not num % 1000:
        print "\r progress: ", num * 100 / tot_1
        sys.stdout.flush()

    if val in dic:
        dup.append(val)

import pdb
pdb.set_trace()
