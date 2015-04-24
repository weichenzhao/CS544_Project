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
from sklearn.linear_model import SGDClassifier
rng = RandomState(42)

from sklearn.decomposition import PCA
from sklearn.decomposition import SparsePCA
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB 

from sklearn.metrics import f1_score

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
     
    Y1=[]
    Y2=[]
    
    # Loop over each review; create an index i that goes from 0 to the length
    # of the movie review list

    
    for i in train:
        buf=[]
        traindata.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(train[i][0]+train[i][1], True)))
        for j in train[i][3].split():
            if j in tag_dic:
               buf.append(tag_dic[j])
        Y1.append(buf)



    for i in test:
        buf=[]
        testdata.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(test[i][0]+test[i][1], True)))
        for j in test[i][3].split():
            if j in tag_dic:
               buf.append(tag_dic[j])
        Y2.append(buf)
    # ****** Create a bag of words from the training set
    #


    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # Tfidf tool.
    vectorizer = CountVectorizer(min_df=0.001)


    X_all=traindata+testdata
    lentrain=len(traindata)

    X = vectorizer.fit_transform(X_all)

    X_train = X[:lentrain]
    X_test = X[lentrain:]

    X1 = X_train.toarray()
    X2 = X_test.toarray()

#    X1 = X_train
#    X2 = X_test

#    clf = GaussianNB()
#   clf=SGDClassifier()
    clf=LinearSVC(random_state=0)
#    clf=RandomForestClassifier(n_estimators = 100)
  #  clf=MultinomialNB()


    classif = OneVsRestClassifier(clf).fit(X1, Y1)
    class_set=classif.classes_
    scores=classif.decision_function(X2)
    Y3=[]
        #    predict=classif.predict(X2)
        
    if len(scores.shape) == 1:
        indices = (scores > 0).astype(np.int)
    else:
        for score in scores:
            buf=[]
            for i in range(9):
                if score[i]>0:
                   buf.append(class_set[i])
            if not buf:
                   indices = np.argmax(score)
                   
                   buf.append(class_set[indices])
            Y3.append(buf)

    for i in Y3:
        print(i)
    print(f1_score(Y3,Y2))
