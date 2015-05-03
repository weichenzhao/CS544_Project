
import operator
import sys
import json
import string
import nltk
import pickle

from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

title = dict()
body = dict()
code = dict()
tag = dict()

stemmer = PorterStemmer()

def stem_tokens(tokens, stemmer):
	stemmed = []
	print(tokens)
	for item in tokens:
		stemmed.append(stemmer.stem(item))
	print(stemmed)
	return stemmed

def tokenize(text):
	global stemmer
	tokens = nltk.word_tokenize(text)
	stems = stem_tokens(tokens, stemmer)
	print(stems)
	return stems


def readFile(inputFile):
	for f in inputFile:
		with open(f) as json_data:
			seg_dict = json.load(json_data)
			for i in seg_dict:
				#print(seg_dict[i])
				title[int(i)] = seg_dict[i][0]
				body[int(i)] = seg_dict[i][1]
				code[int(i)] = seg_dict[i][2]
				t = seg_dict[i][3].split(" ")
				tag[int(i)] = t
#	print(title)
#	print(body)
#	print(code)
#	print(tag[6026061])
#	print(seg_dict)
#	print(body[6026061])




def tf_idf():
	global title
	global tag

	count = 0
	title_token = list()
	tag_title = dict()
	tag_feature = dict()

#	s= ["this sentence has unseen text such as computer but also king lord juliet.", "this is a big mistake!", "mistake"]

	
	for i in title:
		lowers = title[i].lower()
		title_token.append(lowers)
		for t in tag[i]:
			if t not in tag_title:
				tag_title[t] = []
			tag_title[t].append(count)
		count += 1

#	print(title_token)
	print(tag_title)
	
	
	tfidf = TfidfVectorizer(stop_words='english', tokenizer=nltk.word_tokenize)
	tfs = tfidf.fit_transform(title_token)
#	tfs = tfidf.transform(title_token.values)
#	print(tfidf)
#	print(tfs)
	#print(tfidf.get_feature_names())
	feature_names = tfidf.get_feature_names()
#	print(feature_names)
#	print(tfs[0, 5])

	tfs_feature = tfs.toarray()
#	print('pages: ', len(tfs_feature))
#	print('tags: ', len(tag_title))

	for tt in tag_title:
		if tt not in tag_feature:
			tag_feature[tt] = list()
			for i in range(0, len(feature_names)):
				tag_feature[tt].append(0)
		for num in tag_title[tt]:
#			print(title_token[num])
			for i in range(0, len(tfs_feature[num])):
				tag_feature[tt][i] += tfs_feature[num][i]

#	print(len(tag_feature))
#	print('vocabulary: ', len(feature_names))
#	print(tag_feature)
	

#	with open('tag_distance.pickle', 'wb') as f:
#		pickle.dump(tag_feature, f)



	
def main(argv):
	inputFile = argv[1:]
	readFile(inputFile)
	tf_idf()


if __name__ == "__main__":
	main(sys.argv)
