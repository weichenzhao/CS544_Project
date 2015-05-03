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
	global seg_dict
	with open(inputFile) as json_data:
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


def distance(tag_word, feature_names):
	tag_visited = set()
	tag_distance = dict()
#	print(feature_names)
	'''
	for word in feature_names:
		tag_visited.clear()
		for t1 in tag_word:
#			print(t1)
			tag_visited.add(t1)
			for t2 in tag_word:
				if t2 in tag_visited:
					continue
				if (t1, t2) not in tag_distance:
					tag_distance[(t1, t2)] = 0
				if word in tag_word[t1]:
					d1 = tag_word[t1][word]
				else:
					d1 = 0
				if word in tag_word[t2]:
					d2 = tag_word[t2][word]
				else:
					d2 = 0
				tag_distance[(t1, t2)] += abs(d1 - d2)
#				print(t1, ', ', t2, ', ', tag_distance[(t1, t2)])
	'''

	for t1 in tag_word:
		tag_visited.add(t1)
		print(t1)
		for t2 in tag_word:
			if t2 in tag_visited:
				continue
			if (t1, t2) not in tag_distance:
				tag_distance[(t1, t2)] = 0
			for w1 in tag_word[t1]:
				d1 = tag_word[t1][w1]
				if w1 in tag_word[t2]:
					d2 = tag_word[t2][w1]
				else:
					d2 = 0
				tag_distance[(t1, t2)] +=  abs(d1 - d2)
			for w2 in tag_word[t2]:
				if w2 not in tag_word[t1]:
					tag_distance[(t1, t2)] += tag_word[t2][w2]


	print(tag_distance)
#	print(1)
	return tag_distance




def tf_idf():
	global title
	global tag

	count = 0
	title_token = list()
	tag_title = dict()
	tag_word = dict()
	dis = dict()

#	s= ["this sentence has unseen text such as computer but also king lord juliet.", "this is a big mistake!", "mistake"]

	
	for i in title:
		lowers = title[i].lower()
		no_punctuation = lowers.translate(string.punctuation)
		title_token.append(no_punctuation)
		for t in tag[i]:
			if t not in tag_title:
				tag_title[t] = []
			tag_title[t].append(count)
		count += 1

#	print(tag_title)
	
	
	tfidf = TfidfVectorizer(stop_words='english')
	tfs = tfidf.fit_transform(title_token)
#	tfs = tfidf.transform(title_token.values)
#	print(tfidf)
#	print(tfs)
	#print(tfidf.get_feature_names())
	feature_names = tfidf.get_feature_names()
#	print(feature_names)
#	print(tfs[0, 5])


	print(tag_title)
	print('tag nums: ', len(tag_title))
	for tt in tag_title:
		if tt not in tag_word:
			tag_word[tt] = dict()
		for num in tag_title[tt]:
#			print(title_token[num])
			for word in title_token[num].split():
				#print(word)
				if word in feature_names:
					if word not in tag_word[tt]:
						tag_word[tt][word] = 0
					index = feature_names.index(word)
					tag_word[tt][word] += tfs[num, index]
					#print(num, ', ', index)
					#print(tfs[num, index])


#	print(feature_names)
	print(tfs)
	print(tag_word)
	
	dis = distance(tag_word, feature_names)
	with open('tag_distance_0.pickle', 'wb') as f:
		pickle.dump(dis, f)



	
def main(argv):
	inputFile = argv[1]
	readFile(inputFile)
	tf_idf()


if __name__ == "__main__":
	main(sys.argv)
