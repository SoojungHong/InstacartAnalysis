#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:25:18 2018

@author: soojunghong
"""

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
from textblob import Word
from textblob.wordnet import VERB
import csv 
import os
import pandas as pd
from textblob import TextBlob



def readCSV(filePath, fileName): 
    csv_path = os.path.join(filePath,fileName)
    return pd.read_csv(csv_path)        


    
def getProductsInfoInOrder(orderID, data, productInfo, product_dept) :
    order = data[data['order_id'] == orderID] 
    prodList = []
    if(order.empty) : 
        #print("[Warning] There is no order in this data set!!!")
        prodList.append(None)
    else :     
        prodList = order['product_id'].tolist()
    return prodList



def tenMostFrequentlyPurchasedByUser(userID, product, orders, dept) : 
    from collections import Counter
    product_dept = productInfo.merge(dept, on='department_id', how='inner')
    user_products_id = []
    ordersPerUser = orders[orders["user_id"] == userID]
    for ordr in ordersPerUser.order_id : 
        #print(ordr)
        currlist = getProductsInfoInOrder(ordr, data, productInfo, product_dept)
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



def getFullDefinitionFromLastword(product_name):
    #print(type(product_name)) #series type
    #print(product_name)
    #print(product_name.size)
    if(product_name.size == 0) : 
        return Word("None")
    word1 = product_name.values[0]
    product_name = TextBlob(word1.decode('latin-1')) #('utf-8')) #you have to decode 
    wordsLeng = len(product_name.words)
    #decodedProd = (product_name.words[wordsLeng-1]).decode('utf-8')
    #defs = Word(decodedProd).definitions
    defs = Word(product_name.words[wordsLeng-1]).definitions
    if (len(defs) == 0) :
       return Word("None") #there is no definition
      
    return Word(product_name.words[wordsLeng-1]).definitions[0]



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



def showHistogram(d, x_l, x_r, y_b, y_t):
    import numpy as np
    import matplotlib.mlab as mlab
    import matplotlib.pyplot as plt   
    mu, sigma = 100, 15
    n, bins, patches = plt.hist(d, 50, normed=1, facecolor='green', alpha=0.75)
   
    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=1)
    #plt.axis([40, 160, 0, 0.03])
    plt.axis([x_l, x_r, y_b, y_t])#plt.axis([0,6,0,10])
    plt.grid(True)
    plt.show() 
    
    
    
def getShoppingDOW(userID, orders) : 
    #product = readCSV(path_data, data_products)
    #data = readCSV(path_data, data_order_prior)  
    #productInfo = readCSV(path_data, data_products) 
    #dept = readCSV(path_data, data_dept)
    
    ordersPerUser = orders[orders["user_id"] == userID]
    ordersPerUser

    order_dow = ordersPerUser['order_dow']
    order_dow
    showHistogram(order_dow, 0, 6, 0, 10)
    count_early_days = 0 
    count_mid_days = 0
    count_weekend = 0 
    shopDow = ""
    
    for dow in order_dow : 
        if (dow >= 0 & dow <=2) : 
            count_early_days = count_early_days + 1
        if (dow > 2 & dow <= 4) : 
            count_mid_days = count_mid_days + 1
        if (dow >=5 ):
            count_weekend = count_weekend + 1
    
    if(max(count_early_days, count_mid_days, count_weekend) == count_early_days) : 
        print("early week shopper")
        shopDow = "early week shopper"
    if(max(count_early_days, count_mid_days, count_weekend) == count_mid_days) : 
        print("mid shopper")
        shopDow = "mid shopper"
    if(max(count_early_days, count_mid_days, count_weekend) == count_weekend) :
        print("weekend shopper")
        shopDow = "weekend shopper"
     
    return shopDow  
    


def getShoppingHour(userID, orders) : 
    #product = readCSV(path_data, data_products)
    #data = readCSV(path_data, data_order_prior)  
    #productInfo = readCSV(path_data, data_products) 
    #dept = readCSV(path_data, data_dept)
    
    ordersPerUser = orders[orders["user_id"] == userID]
    ordersPerUser

    order_hour = ordersPerUser['order_hour_of_day']
    order_hour
    
    showHistogram(order_hour, 0, 25, 0, 10)

    count_early_bird = 0 
    count_daytime_shopper = 0
    count_evening_shopper = 0
    count_night_owl = 0
    shopHour = ""
    
    for hr in order_hour : 
        if (hr >= 5 & hr <= 9) : 
            count_early_bird = count_early_bird + 1
        if (hr > 22 & hr <= 4) : 
            count_night_owl = count_night_owl + 1
        if (hr >= 10 & hr <= 18 ):
            count_daytime_shopper = count_daytime_shopper + 1
        if (hr >= 19 & hr <= 21) : 
            count_evening_shopper = count_evening_shopper + 1
    
    maxCount = max(count_early_bird, count_night_owl, count_daytime_shopper, count_evening_shopper ) 
    if( maxCount == count_early_bird) : 
        print("early bird shopper")
        shopHour = "early bird shopper"
    if(maxCount == count_night_owl) : 
        print("night owl shopper")
        shopHour = "night owl shopper"
    if(maxCount == count_daytime_shopper) :
        print("day shopper")
        shopHour = "day shopper"
    else :
        print("evening shopper")
        shopHour = "evening shopper"
                
    return shopHour    


    
#------------------------------------------------------------------------
# Create User Profile : <userID> <userProfileName> <shopDay> <shopHour>
#------------------------------------------------------------------------
import pandas as pd
path_data = "/Users/soojunghong/Documents/safariML/ML_python/kaggle/InstacartAnalysis/data/"
data_aisle = "aisles.csv"
data_dept = "departments.csv"
data_order_prior = "order_products_prior.csv"
data_order_train = "order_products_train.csv"
data_orders = "orders.csv"
data_products = "products.csv"

data = readCSV(path_data, data_order_prior) 
productInfo = readCSV(path_data, data_products)
product = readCSV(path_data, data_products)
orders = readCSV(path_data, data_orders)
dept = readCSV(path_data, data_dept)

# initializa dataframe 
d = {'userID':[], 'userProfileName':[], 'userShopDay':[], 'userShopHour':[]}
df = pd.DataFrame(data = d)
df

for i in range(1,200): 
    row = pd.DataFrame({'userID':[i], 'userProfileName':[topicOfUser(i, product, orders, dept)], 'userShopDay':[getShoppingDOW(i, orders)], 'userShopHour':[getShoppingHour(i, orders)]})
    df = df.append(row)

df    
#df = df.append(row2)
#df