import sys
import json
import pickle
import string
import nltk

from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC

from sklearn.metrics import f1_score

tag_dict = list()

seg_dict = dict()
tags = list()
body = list()
code = list()
title = list()

seg_dict_test = dict()
tags_test = list()
body_test = list()
code_test = list()
title_test = list()

def readTag(tagFile):
#	print("reading Tag:")
	with open(tagFile) as f:
		for tag in f:
			if len(tag_dict) >= 100:
				break
			tag_dict.append(tag.split()[0])
#	print(tag_dict)

def readFile(trainFile, testFile):

#	print("reading trainging file:")

	tag = list()

#	for f in trainFile:
	with open(trainFile) as json_data:
		seg_dict = json.load(json_data)
		for i in seg_dict:
			flag = 0;
			ts = seg_dict[i][3].split(" ")
			tag = list()
			for t in ts:
				if t in tag_dict:
					tag.append(tag_dict.index(t))
					flag = 1
			if flag == 1:
				tags.append(tag)
				title.append(seg_dict[i][0])
				body.append(seg_dict[i][1])
				code.append(seg_dict[i][2])

#	print("reading test file: ")
	with open(testFile) as json_data:
		seg_dict_test = json.load(json_data)
		for i in seg_dict_test:
			flag = 0;
			ts = seg_dict_test[i][3].split(" ")
			tag = list()
			for t in ts:
				if t in tag_dict:
					tag.append(tag_dict.index(t))
					flag = 1
			if flag == 1:
				tags_test.append(tag)
				title_test.append(seg_dict_test[i][0])
				body_test.append(seg_dict_test[i][1])
				code_test.append(seg_dict_test[i][2])
	print("###################### test tags: #########################")
	print(tags_test)

	pkl_file = open('input_20k_100.pkl', 'wb')
	data = [tags, body, code, title, tags_test, body_test, code_test, title_test, tag_dict]
	pickle.dump(data, pkl_file)
	pkl_file.close()
	
#	print(tags)
#	print(body)
#	print(code)
#	print(title)
##################################################### main ##################################################

def main(argv):
	tagFile = argv[1]
	trainFile = argv[2]
	testFile = argv[3]

	print("train file: ", trainFile, "")
	print("test file: ", testFile, "")

	readTag(tagFile)
	readFile(trainFile, testFile)
#	tf_idf_body()
#	tf_idf_code()
#	BOW_body()
#	BOW_code()
#	predict_title()



if __name__ == '__main__':
	main(sys.argv)


