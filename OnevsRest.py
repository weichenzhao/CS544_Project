#!/usr/bin/env python

#  Author: Angela Chapman
#  Date: 8/6/2014
#
#  This file contains code to accompany the Kaggle tutorial
#  "Deep learning goes to the movies".  The code in this file
#  is for Part 1 of the tutorial on Natural Language Processing.
#
# *************************************** #

import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from KaggleWord2VecUtility import KaggleWord2VecUtility
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import cross_validation
from sklearn.datasets import make_multilabel_classification
import pandas as pd
import numpy as np
import json
import sys
import time

from collections import defaultdict
from sklearn.cluster import KMeans
from numpy.random import RandomState
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
rng = RandomState(42)

from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC

if __name__ == '__main__':
    input1=sys.argv[1]   # train data
    input2=sys.argv[2]   # test data
    tagdic=sys.argv[3]   # dictionary for tag 2000

    train=json.load(open(input1))
    test=json.load(open(input2))
    
    tag_dic=json.load(open(tagdic))


    # Initialize an empty list to hold the clean reviews
    traindata = []
    testdata = []
    tag=defaultdict()
    tag_line=defaultdict()
 
    traindata_final = []      
    Y=[]
    # Loop over each review; create an index i that goes from 0 to the length
    # of the movie review list

    c=0
    
    for i in train:
        traindata.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(train[i][0], False)))
        for j in train[i][3].split():
            if j in tag_dic:
                if c not in tag:
                   tag[c]=[]
                else:
                    tag[c].append(tag_dic[j])
        c+=1



    for i in test:
        testdata.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(test[i][0], False)))
    # ****** Create a bag of words from the training set
    #


    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # Tfidf tool.
        tfv = TfidfVectorizer(min_df=3,  max_features=None,
                          strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
                          ngram_range=(1, 2), use_idf=1,smooth_idf=1,sublinear_tf=1,
                          stop_words = 'english')


    X_all = traindata + testdata
    lentrain = len(traindata)


#tfv.fit(X_all)

    X_all = tfv.fit_transform(X_all)
    X_all = X_all.toarray()

#    for xx in X_all[0]:
#        print xx

    X = X_all[:lentrain]
    X_test = X_all[lentrain:]


    for x in tag:
        traindata_final.append(X[x])

#    print traindata_final[:3]

    for x in tag:
        Y.append(tag[x])

    traindata_final = PCA(n_components=10).fit_transform(traindata_final)

    classif = OneVsRestClassifier(LinearSVC(random_state=0),n_jobs=-1).fit(traindata_final1, Y)
#y_score=classif.fit(X, Y).decision_function(X_test)
    
    y_score=classif.fit(traindata_final, Y)
    predict=classif.predict(X_test)
    for y in predict:
        print(y)
#print(max(y))
