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



#------------------------------
# get definition from product
#------------------------------

import csv 
import os
import pandas as pd
     
def getProductsInfoInOrder(orderID, data, productInfo, product_dept) :
    #data = readCSV(path_data, data_order_prior)  
    #productInfo = readCSV(path_data, data_products)
    order = data[data['order_id'] == orderID] 
    if(order.empty) : 
        print("There is no order in this data set")
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
    word1 = product_name.values[0]
    product_name = TextBlob(word1)
    wordsLeng = len(product_name.words)
    print(product_name.words[wordsLeng-1])
    print(Word(product_name.words[wordsLeng-1]).definitions)    



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
    product_name_len = len(product_name.words)
    if(product_name_len > 0) :
            product_noun = product_name.words[product_name_len - 1]
            noun = Word(product_noun)
            nounDesc = noun.definitions
    
    firstDesc = ""
    if(len(nounDesc) > 0) :
        firstDesc = nounDesc[0]
  
    return firstDesc


        
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
        product_names_desc = []
        for n in user_products_names : 
            product_names_desc.append(getProductFirstDescOfNoun(n))
    
    #get most frequent words from all descriptions 
    eg = TextBlob(product_names_desc[0])
    print(eg.noun_phrases) 
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

#---------------------------------------------------------------------------
# for all users, get 3 most frequently purchased products, 
#                and get definitions of products and extract relevant words 
#---------------------------------------------------------------------------
# userID starts from 1 to 206209
     
product = readCSV(path_data, data_products)
orders = readCSV(path_data, data_orders)
dept = readCSV(path_data, data_dept)

for userID in range(1, 2):#206209) : 
    print("userID : " + str(userID))
    mProduct = threeMostFrequentlyPurchasedByUser(userID, product, orders, dept)#.product_name
    #print(mProduct[2].product_name)
    #print(getProductFirstDescOfNoun(mProduct[2].product_name))
    print(getMostFreqWordsInProductDefinition(userID, product, orders, dept))


#----------------------
# Create User Profile
#----------------------
import pandas as pd
d = {'userID' : [1,2,3], 'userProfileName': ['organic', 'lifegoods', 'meatperson'], 'shoppingHour' : ['morning', 'afternoon', 'evening']}
df = pd.DataFrame(data=d)
df

