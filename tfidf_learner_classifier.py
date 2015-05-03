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
	
#	print(tags)
#	print(body)
#	print(code)
#	print(title)

def tokenize(text):
	no_punctuation = text.translate(string.punctuation)
	return no_punctuation.split

def tf_idf_body():
#	print("tf_idf body trainging:")
	tfidf = TfidfVectorizer(stop_words='english', tokenizer=nltk.word_tokenize)
	tfs = tfidf.fit_transform(body)
#	tfs_feature = tfs.toarray()
	features_name = tfidf.get_feature_names()

#	print("tf_idf body test:")
	test_feature = tfidf.transform(body_test)
#	print(tfs_feature)
#	print(len(features_name))
#	print(tags_test)

################## learn ####################
	model = learn(tfs)

################## classify #################
	print("############\ttags predicted by body (tfidf) \t############")
	classify(model, test_feature, tags_test)

def tf_idf_code():
#	print("tf_idf code training:")
	tfidf = TfidfVectorizer(stop_words=None, tokenizer=nltk.word_tokenize)
#	print(code)
	tfs = tfidf.fit_transform(code)
#	tfs_feature = tfs.toarray()
	features_name = tfidf.get_feature_names()

#	print("tf_idf code test:")
	test_feature = tfidf.transform(code_test)
#	print(tfs_feature)
#	print(len(features_name))
#	print(tags_test)

################## learn ####################
	model = learn(tfs)

################## classify #################
	print("############\ttags predicted by code(tfidf):\t############")
	classify(model, test_feature, tags_test)

def BOW_body():
	print("bag_of_words body train: ")
	bow = CountVectorizer(stop_words='english', tokenizer=nltk.word_tokenize)
	bag = bow.fit_transform(body)

	print("bag of wrods test: ")
	test_feature = bow.transform(body_test)

	model = learn(bag)

	print("############\ttags predicted by body(bag of words):\t############")
	classify(model, test_feature, tags_test)

def BOW_code():
	print("bag_of_words code train: ")
	bow = CountVectorizer(stop_words=None, tokenizer=nltk.word_tokenize)
	bag = bow.fit_transform(code)

	print("bag of wrods test: ")
	test_feature = bow.transform(code_test)

	model = learn(bag)

	print("############\ttags predicted by code(bag of words):\t############")
	classify(model, test_feature, tags_test)

def predict_title():
	print("classifiy title: ")
	tag_predict = list()
	for line in title_test:
		lowers = line.lower()
		no_punctuation = lowers.translate(string.punctuation)
		tokens = no_punctuation.split()
#		print(tokens)
		t = list()
		for token in tokens:
			if token in tag_dict:
#				print(token)
				t.append(tag_dict.index(token))
		tag_predict.append(t)
	print("############\ttags predicted by title:\t############")
	print(tag_predict)


def learn(tfs_feature):
#	print("PCA")
#	print(tfs_feature)
#	traindata_final = PCA(n_components=10000).fit_transform(tfs_feature)
#	print(traindata_final)
	print("learning: ")
	model = OneVsRestClassifier(LinearSVC(random_state=0)).fit(tfs_feature, tags)
#	model = OneVsRestClassifier(SGDClassifier()).fit(tfs_feature, tags)
	return model

def classify(model, test_feature, tags_test):
	print("predicting: ")
	tag_predict = model.predict(test_feature)
	print(tag_predict)
	result = f1_score(tags_test, tag_predict, average='weighted')
	print("f-score: ", result)
	return tag_predict
	



##################################################### main ##################################################

def main(argv):
	tagFile = argv[1]
	trainFile = argv[2]
	testFile = argv[3]

	print("train file: ", trainFile, "")
	print("test file: ", testFile, "")

	readTag(tagFile)
	readFile(trainFile, testFile)
	tf_idf_body()
	tf_idf_code()
	BOW_body()
	BOW_code()
	predict_title()
#	test(testFile)
#	learn()


if __name__ == '__main__':
	main(sys.argv)


