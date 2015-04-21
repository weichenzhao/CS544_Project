import simplejson
import sys

"""
    HOW TO USE:
        python fscore.py result_1.txt

    DECODE PROBLEM:
        1. is seems JSON only takes '[', ']' for lists
        2. JSON requires ',' can only be placed between elements

    FORMAT CHANGE:
        refer to the result_1.txt, which line 9 is the standard array
        and line 12 is the prediction array

    CALCULATION:
        precision is calculated use classification (number of predictions)
        to devide correct classification (predicted tag appeared in 
        standard).
        recall is calculated using the similar way, devided by number of
        tags appeared in standard
"""
fin = sys.argv[1]
f = open(fin, 'r')

num = 0
for line in f:
    num += 1
    if num == 9:
        # test
        #print line
        standard = simplejson.loads(line)
    if num == 12:
        # result
        line = line.replace('(', '[')
        line = line.replace(')', ']')
        line = line.replace(',]', ']')
        #print line
        result = simplejson.loads(line)

correct = 0
classify = 0
belongs = 0

# correct clssify / classified
for i in range(len(result)):
    for predict in result[i]:
        classify += 1
        if predict in standard[i]:
            correct += 1

# belongs
for i in range(len(standard)):
    for elem in standard[i]:
        belongs += 1

#import pdb
#pdb.set_trace()

precision = correct * 100.0 / classify
recall = correct * 100.0 / belongs
fscore = 2 * precision * recall / ( precision + recall )

print "Presicion: ", precision
print "Recall: ", recall
print "f-score: ", fscore
