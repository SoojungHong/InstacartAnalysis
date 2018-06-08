#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 23:15:00 2018

@author: soojunghong
"""
#-----------------
# Import textblob 
#-----------------
from textblob import TextBlob
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
wiki.tags


#------------------------
# Text analysis example
#------------------------
from textblob import TextBlob
blob = TextBlob("ITP is a two-year graduate program located in the Tisch School of the Arts. Perhaps the best way to describe us is as a Center for the Recently Possible.")

for sentence in blob.sentences:
    print(sentence)

from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
documents = dataset.data
documents


#------------------------------
# get definition from product
#------------------------------

import csv 
import os
import pandas as pd
     
def getProductsInfoInOrder(orderID, data, productInfo, product_dept) :
    order = data[data['order_id'] == orderID] 
    prodList = []
    if(order.empty) : 
        #print("[Warning] There is no order in this data set!!!")
        prodList.append(None)
    else :     
        prodList = order['product_id'].tolist()
    return prodList

     
def printAllProductsInOrder(orderID, data, productInfo) :
    #data = readCSV(path_data, data_order_prior)  
    #productInfo = readCSV(path_data, data_products)
    products = []
    order = data[data['order_id'] == orderID] 
    if(order.empty) : 
        print("There is no order in this data set")
    prodList = order['product_id'].tolist()
    for ord in prodList : 
        prod = productInfo[productInfo["product_id"] == ord].product_name
        print(prod)
        products.append(prod)
    return products


def readCSV(filePath, fileName): 
    csv_path = os.path.join(filePath,fileName)
    return pd.read_csv(csv_path)        


def getFullDefinition(product_name):
    word1 = product_name.values[0]
    product_name = TextBlob(word1)
    #wordsLeng = len(product_name.words)
    for subPro in product_name.words :
        print(Word(subPro).definitions)
        

def getFullDefinitionFromLastword(product_name):
    #print(type(product_name)) #series type
    #print(product_name)
    #print(product_name.size)
    if(product_name.size == 0) : 
        return Word("None")
    word1 = product_name.values[0]
    product_name = TextBlob(word1)
    wordsLeng = len(product_name.words)
    defs = Word(product_name.words[wordsLeng-1]).definitions
    if (len(defs) == 0) :
       return Word("None") #there is no definition
      
    return Word(product_name.words[wordsLeng-1]).definitions[0]


def getProductDescOfAdjective(prod) : 
    productName = prod.values[0]
    productName
    product_name = TextBlob(productName)
    #product_name_len = len(product_name.words)
    product_adj = product_name.words[0]
    adj = Word(product_adj)
    adjDesc = adj.definitions

    return adjDesc



def getProductDescOfNoun(prod) : 
    productName = prod.values[0]
    productName
    product_name = TextBlob(productName)
    product_name_len = len(product_name.words)
    product_noun = product_name.words[product_name_len - 1]
    noun = Word(product_noun)
    nounDesc = noun.definitions

    return nounDesc



def getProductFirstDescOfNoun(prod) : 
    productName = prod.values[0]
    productName
    product_name = TextBlob(productName)
    
    print(product_name.words)
    
    
    """
    wordList = []
    # line = line.replace(';', ':')
    for w in product_name.words : 
        w = w.decode.encode('utf-8')
        w = w.replace('-', '')
        wordList.append(w)
     
    product_name_len = len(wordList)
    print(product_name_len)
    print(wordList)
    product_noun = wordList[product_name_len - 1]
    noun = Word(product_noun)
    nounDesc = noun.definitions
    print(nounDesc[0].decode.encode('utf-8')) 
    return nounDesc[0].decode.encode('utf-8') 
    """

        
"""
def mostFrequentlyPurchasedByUser(userID) : 
    from collections import Counter
    product = readCSV(path_data, data_products)
    orders = readCSV(path_data, data_orders)
    dept = readCSV(path_data, data_dept)
    product_dept = productInfo.merge(dept, on='department_id', how='inner')
    user_products_id = []
    ordersPerUser = orders[orders["user_id"] == userID]
    for ordr in ordersPerUser.order_id : 
        #print(ordr)
        currlist = getProductsInfoInOrder(ordr, data, productInfo, product_dept)
        for p in currlist : 
            #print(product[product["product_id"] == p].product_name)  
            user_products_id.append(p)
    #print(user_products_id)
    c = Counter(user_products_id)
    mostfreq_id = c.most_common(1)
    #print(mostfreq_id)
    mostfreq =product.loc[product['product_id'] == mostfreq_id[0][0]] 
    return mostfreq
"""   


def threeMostFrequentlyPurchasedByUser(userID, product, orders, dept) : 
    from collections import Counter
#    product = readCSV(path_data, data_products)
#    orders = readCSV(path_data, data_orders)
#    dept = readCSV(path_data, data_dept)
    product_dept = productInfo.merge(dept, on='department_id', how='inner')
    user_products_id = []
    ordersPerUser = orders[orders["user_id"] == userID]
    for ordr in ordersPerUser.order_id : 
        #print(ordr)
        currlist = getProductsInfoInOrder(ordr, data, productInfo, product_dept)
        #print(currlist)
        for p in currlist : 
            #print(product[product["product_id"] == p].product_name)  
            user_products_id.append(p)
    #print(user_products_id)
    c = Counter(user_products_id)
    mostfreq_id = c.most_common(1) # 1 most frequent 
    mostfreq_id1 = c.most_common(2) # 2 most frequent
    mostfreq_id2 = c.most_common(3) # 3 most frequent
    
    threeMost = []
    mostfreq =product.loc[product['product_id'] == mostfreq_id[0][0]] 
    threeMost.append(mostfreq) 
    secondfreq =product.loc[product['product_id'] == mostfreq_id1[1][0]] 
    threeMost.append(secondfreq) 
    thirdfreq =product.loc[product['product_id'] == mostfreq_id2[2][0]] 
    threeMost.append(thirdfreq)
    return threeMost



def tenMostFrequentlyPurchasedByUser(userID, product, orders, dept) : 
    from collections import Counter
    product_dept = productInfo.merge(dept, on='department_id', how='inner')
    user_products_id = []
    ordersPerUser = orders[orders["user_id"] == userID]
    for ordr in ordersPerUser.order_id : 
        #print(ordr)
        currlist = getProductsInfoInOrder(ordr, data, productInfo, product_dept)
        print(currlist)
        if(len(currlist) != 0) : 
            for p in currlist : 
                #print(product[product["product_id"] == p].product_name)  
                user_products_id.append(p)
    #print(user_products_id)
    c = Counter(user_products_id)
    tenMost = []
    if (len(c) > 10) : 
        for i in range(1,11) : 
            prod = c.most_common(i)
            tenMost.append(product.loc[product['product_id'] == prod[i-1][0]])
    else : 
        return "None"
    return tenMost
    
    """    
    mostfreq_id = c.most_common(1) # 1 most frequent 
    mostfreq_id1 = c.most_common(2) # 2 most frequent
    mostfreq_id2 = c.most_common(3) # 3 most frequent
    
    threeMost = []
    mostfreq =product.loc[product['product_id'] == mostfreq_id[0][0]] 
    threeMost.append(mostfreq) 
    secondfreq =product.loc[product['product_id'] == mostfreq_id1[1][0]] 
    threeMost.append(secondfreq) 
    thirdfreq =product.loc[product['product_id'] == mostfreq_id2[2][0]] 
    threeMost.append(thirdfreq)
    return threeMost
    """
   

def MostFrequentlyPurchasedByUser(userID, product, orders, dept) : 
    from collections import Counter
#    product = readCSV(path_data, data_products)
#    orders = readCSV(path_data, data_orders)
#    dept = readCSV(path_data, data_dept)
    product_dept = productInfo.merge(dept, on='department_id', how='inner')
    user_products_id = []
    ordersPerUser = orders[orders["user_id"] == userID]
    for ordr in ordersPerUser.order_id : 
        #print(ordr)
        currlist = getProductsInfoInOrder(ordr, data, productInfo, product_dept)
        #print(currlist)
        for p in currlist : 
            #print(product[product["product_id"] == p].product_name)  
            user_products_id.append(p)
    #print(user_products_id)
    c = Counter(user_products_id)
    mostfreq_id = c.most_common(1) # 1 most frequent 
    print(mostfreq_id)
    
    mostfreq =product.loc[product['product_id'] == mostfreq_id[0][0]] 
    return mostfreq



def getMostFreqWordsInProductDefinition(userID, product, orders, dept):
    #from collections import Counter
    user_products_names = []
    product_names_desc = []
    product_dept = productInfo.merge(dept, on='department_id', how='inner')
    ordersPerUser = orders[orders["user_id"] == userID]
    for ordr in ordersPerUser.order_id : 
        #print(ordr)
        currlist = getProductsInfoInOrder(ordr, data, productInfo, product_dept)
        for p in currlist : 
            #print(product[product["product_id"] == p].product_name)  
            pName = product[product["product_id"] == p].product_name
            user_products_names.append(pName)
        #print(user_products_names)
        #product_names_desc = []
        for n in user_products_names : 
            product_names_desc.append(getProductFirstDescOfNoun(n))
    
    #get most frequent words from all descriptions 
    #eg = TextBlob(product_names_desc[1])
    #print(eg.noun_phrases) 
    
    all_nouns = []
    for desc in product_names_desc : 
        tmp_desc = TextBlob(desc)
        #print(tmp_desc.noun_phrases)
        for phr in tmp_desc.noun_phrases : 
            all_nouns.append(phr)
    #print(type(all_nouns)) #list - probably WordList
    from collections import Counter
    c = Counter(all_nouns)   
    print(c.most_common(1))
    
    return product_names_desc           
  
    
#---------
# data 
#---------        
path_data = "/Users/soojunghong/Documents/safariML/ML_python/kaggle/InstacartAnalysis/data/"
data_aisle = "aisles.csv"
data_dept = "departments.csv"
data_order_prior = "order_products_prior.csv"
data_order_train = "order_products_train.csv"
data_orders = "orders.csv"
data_products = "products.csv"

readCSV(path_data, data_orders)
readCSV(path_data, data_products)
data = readCSV(path_data, data_order_prior)  
data
productInfo = readCSV(path_data, data_products)
productInfo   
products = printAllProductsInOrder(9, data, productInfo) #number of products : 49687
products
products[0]


#------------------------------------
# for each product, get definition
#------------------------------------
from textblob import Word
from textblob.wordnet import VERB

productName = products[0].values[0]
productName
product_name = TextBlob(productName)
type(product_name.words)
product_name_len = len(product_name.words)
product_name_len
product_adj = product_name.words[0]
product_adj
product_noun = product_name.words[product_name_len - 1]
product_noun
# ToDo : if the product name contains, comma, the noun should be string before the comma

adj = Word(product_adj)
adj.definitions

noun = Word(product_noun)
noun.definitions

# test of getting description of adjective of product and description of noun in product name
products[1]    
getFullDefinition(products[1])    
descNoun = getProductDescOfNoun(products[1])
len(descNoun)
descNoun[0]

descAdj = getProductDescOfAdjective(products[1])
descAdj[0]

products[3]
getFullDefinitionFromLastword(products[3])


#-------------------------------
# Bag-of-Words in Scikit-learn 
#-------------------------------
from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
documents = dataset.data
documents

from sklearn.feature_extraction.text import CountVectorizer 
vectorizer = CountVectorizer()
A = vectorizer.fit_transform(documents)
print(A)

#list all terms and associated dictionary which maps each unique term to a corresponding column in the matrix
terms = vectorizer.get_feature_names()
len(terms) #how many terms in the column 

vocab = vectorizer.vocabulary_
vocab["world"] #which column corresponds to a term 

#--------------------------------------------------------
# TF-IDF (term frequency, Inversed Document Frequency)
#--------------------------------------------------------
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
A = vectorizer.fit_transform(documents)
print(A)

from sklearn import decomposition
k = 10
model = decomposition.NMF(n_components = k, init = "nndsvd") # initialize with SVD
W = model.fit_transform(A)
H = model.components_

print(W)
print(H)

#--------------------------------------------------------------------------
# idea : get description of all products that user ordered and find topic 
#--------------------------------------------------------------------------
import pandas as pd;
import numpy as np;
import scipy as sp;
import sklearn;
import sys;
from nltk.corpus import stopwords;
import nltk;
from gensim.models import ldamodel
import gensim.corpora;
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer;
from sklearn.decomposition import NMF;
from sklearn.preprocessing import normalize;
import pickle;
import re;

def get_lda_topics(model, num_topics):
    word_dict = []
    for i in range(num_topics):
        words = model.show_topic(i, topn=20)
        
        for i in words : 
            #print i[0]
            word_dict.append(i[0])
        #word_dict['Topic # ' + '{:02d}'.format(i+1)] = [i[0] for i in words]; #format(i+1) is to start topic index from 1 (since 0 is CS people' index )
    return pd.DataFrame(word_dict)


def findTopic(data) : #data_text is dataframe 
    data_text = data[['favorite_product_desc']]; # we only need text column from the original data
    data_text = data_text.astype('str')
   
    for idx in range(len(data_text)):
        #remove stop words
        # org #data_text.iloc[idx]['favorite_product_desc'] = [word for word in data_text.iloc[idx]['favorite_product_desc'].split(' ') if word not in stopwords.words()]
        data_text.iloc[idx]['favorite_product_desc'] = [word for word in data_text.iloc[idx]['favorite_product_desc'].split(' ') if word not in stopwords.words()]
    
        #print logs to monitor output
        #if idx % 1000 == 0:
        #    sys.stdout.write('\rc = ' + str(idx) + ' / ' + str(len(data_text)));
    
    documents = []
    for value in data_text.iloc[0:].values:
        # add into list 'documents', value is narray 
      
        # value is narray
        for i in range(len(value)):   #print(value[i][0])
            for j in range(len(value[i])) :
                value[i][j] = re.sub('[^a-zA-Z0-9-_*.]', '', value[i][j])
        
        documents.append(value)

    train_headlines = [value[0] for value in data_text.iloc[0:].values];  
    
    num_topics = 10
    id2word = gensim.corpora.Dictionary(train_headlines)

    corpus = [id2word.doc2bow(text) for text in train_headlines] #doc2bow : The function doc2bow() simply counts the number of occurrences of each distinct word, converts the word to its integer word id and returns the result as a sparse vector.

    lda = ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=num_topics)
    ret = get_lda_topics(lda, num_topics) #ret is list type
    #print(ret) 
    return ret

"""
# similarity between definition
from textblob.wordnet import Synset
octopus = Synset(products[1].values[0]+'.n.01')
shrimp = Synset('shrimp.n.03')
octopus.path_similarity(shrimp)

prod = TextBlob(products[1].values[0])
prod.words
num = len(prod.words)
num
Word(prod.words[num-1]).definitions 
Word(prod.words[num-1]).synsets  
mush1 = Synset('mushroom.n.01')
mush2 = Synset('mushroom.n.02')
mush1.path_similarity(mush2)
"""

"""
#---------------------------------------------------------------------------
# for all users, get 3 most frequently purchased products, 
#                and get definitions of products and extract relevant words 
#---------------------------------------------------------------------------
"""
# userID starts from 1 to 206209

#-------------------------------------------------------------------------------
# for each user, get their 3 most frequently purchased products 
# and find out the topic out of it, this topic will be user profile's name
#-------------------------------------------------------------------------------     
product = readCSV(path_data, data_products)
orders = readCSV(path_data, data_orders)
dept = readCSV(path_data, data_dept)
 
# create dataframe df 
import pandas as pd
import numpy as np
df = pd.DataFrame(columns=('userID', 'favorite_product_desc'))
df

userID = 1
mProduct = threeMostFrequentlyPurchasedByUser(userID, product, orders, dept)
type(mProduct) #list type
for p in mProduct : 
    #print(p.product_name)
    #print(getFullDefinitionFromLastword(p.product_name))
    defPROD = getFullDefinitionFromLastword(p.product_name) #products[1]) 
    if(defPROD != '') :
        df = df.append({'userID':userID, 'favorite_product_desc':defPROD}, ignore_index=True)
        

df    
topics = findTopic(df)
type(topics)
topics.iloc[0]
 

#-----------------------------------------------------------------------------------
# Find out topic from all users by analyzing 10 most frequently purchased products
# total number of users : 206209
#-----------------------------------------------------------------------------------
userID = 4
mProduct = tenMostFrequentlyPurchasedByUser(userID, product, orders, dept)
mProduct
for p in mProduct : 
    #print(p.product_name)
    #print(getFullDefinitionFromLastword(p.product_name))
    defPROD = getFullDefinitionFromLastword(p.product_name) #products[1]) 
    if(defPROD != '') :
        df = df.append({'userID':userID, 'favorite_product_desc':defPROD}, ignore_index=True)
        
df
# topics.iloc[0] 

from collections import Counter
topics = findTopic(df)
myList = topics.iloc[:, 0]
topicList = myList.tolist()
c = Counter(topicList)
mostfreq_id = c.most_common(1) # 1 most frequent - #instead of the 0th topic, get the top most frequent topic
mostfreq_id

    
#------------------------------------------------------------------------------------------------
# Based on customer's top 10 most frequent purchased product, topic modeling the topic of user
#------------------------------------------------------------------------------------------------
def topicOfUser(userID, product, orders, dept) :
    # create dataframe df 
    import pandas as pd
    df = pd.DataFrame(columns=('userID', 'favorite_product_desc'))
    
    mProduct = tenMostFrequentlyPurchasedByUser(userID, product, orders, dept)
    if(mProduct != "None") : 
        for p in mProduct : 
            defPROD = getFullDefinitionFromLastword(p.product_name) #products[1]) 
            if(defPROD != '') :
                df = df.append({'userID':userID, 'favorite_product_desc':defPROD}, ignore_index=True)
    
        from collections import Counter
        topics = findTopic(df)
        myList = topics.iloc[:, 0]
        topicList = myList.tolist()
        c = Counter(topicList)
        mostfreq_id = c.most_common(1) # 1 most frequent - #instead of the 0th topic, get the top most frequent topic
        return mostfreq_id
 
    else :
        return "None"
    
# find out topic of all customers and put it in their profile    
product = readCSV(path_data, data_products)
orders = readCSV(path_data, data_orders)
dept = readCSV(path_data, data_dept)

#ToDo
for i in range(1, 20): #:206209) : 
    print(topicOfUser(i, product, orders, dept))    
   

"""    
#----------------------
# Create User Profile
#----------------------
import pandas as pd
d = {'userID' : [1,2,3], 'userProfileName': ['organic', 'lifegoods', 'meatperson'], 'shoppingHour' : ['morning', 'afternoon', 'evening']}
df = pd.DataFrame(data=d)
df
"""
