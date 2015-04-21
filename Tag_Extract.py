# this code is to directly extrac tag from title
import json
import sys
from collections import defaultdict

input=sys.argv[1]   # train data
tag_dic=sys.argv[2]   # dictionary for tag 100

data=json.load(open(input))
dic=json.load(open(tag_dic))

Y=defaultdict()

for i in data:
    title=data[i][0]
    Y[i]=[]
    for j in title.split():
        if j in dic:
            Y[i].append(dic[j])
for z in Y:
	print(z,Y[z])
