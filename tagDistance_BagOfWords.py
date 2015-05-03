import sys
import json
import string
import nltk
import pickle

from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

title = dict()
body = dict()
code = dict()
tag = dict()
tag_title = dict()
tag_list = list()


def readFile(inputFile):
	with open(inputFile) as json_data:
		seg_dict = json.load(json_data)
		for i in seg_dict:
			#print(seg_dict[i])
			title[int(i)] = seg_dict[i][0]
			body[int(i)] = seg_dict[i][1]
			code[int(i)] = seg_dict[i][2]
			ts = seg_dict[i][3].split(" ")
			tag[int(i)] = ts
			for t in ts:
				if t not in tag_title:
					tag_title[t] = seg_dict[i][0].lower()
				else:
					tag_title[t] = tag_title[t] + ' ' + seg_dict[i][0].lower()

	j = 0
	for i in tag_title:
#		print(i, ': ', tag_title[i])
		tag_list.append(i)

#	print(tag)
	print(len(tag_list))
	print(len(tag_title))
#	print(tag_title)
#	print(title)
#	print(body)
#	print(code)
#	print(tag[6026061])
#	print(seg_dict)
#	print(body[6026061])

def distance(bag):
	tag_distance = dict()
#	print(feature_names)
	
	for i in range(0, len(tag_list)):
		t1 = tag_list[i]
		print(t1)
		for j in range(i+1, len(tag_list)):
			t2 = tag_list[j]
			if (t1, t2) not in tag_distance:
				tag_distance[(t1, t2)] = 0

			for w1 in bag[t1]:
				d1 = bag[t1][w1]
				if w1 in bag[t2]:
					d2 = bag[t2][w1]
				else:
					d2 = 0
				tag_distance[(t1, t2)] +=  abs(d1 - d2)
#				print(t1,', ', t2, ', ', tag_distance[(t1, t2)])
			for w2 in bag[t2]:
				if w2 not in bag[t1]:
					tag_distance[(t1, t2)] += bag[t2][w2]
#				print(t1,', ', t2, ', ', tag_distance[(t1, t2)])


	print(tag_distance)
#	print(1)
	return tag_distance


def bag_of_words():
	vec = CountVectorizer(stop_words='english', tokenizer=nltk.word_tokenize)
	bag = vec.fit_transform(tag_title.values())
	bag_matrix = dict()
#	print(bag)
#	print(vec.get_feature_names())
#	print(len(vec.get_feature_names()))

	tag_number = bag.nonzero()[0]
	feature = bag.nonzero()[1]
	for i in range(0, len(tag_number)):
		x = tag_number[i]
		y = feature[i]
		if tag_list[x] not in bag_matrix:
			bag_matrix[tag_list[x]] = dict()
		bag_matrix[tag_list[x]][y] = bag[x, y]
#	print(bag_matrix)
	dis = distance(bag_matrix)
	with open('tag_distance_bag_0.pickle', 'wb') as f:
		pickle.dump(dis, f)

	
def main(argv):
	inputFile = argv[1]
	readFile(inputFile)
	bag_of_words()
#	tf_idf()


if __name__ == "__main__":
	main(sys.argv)
