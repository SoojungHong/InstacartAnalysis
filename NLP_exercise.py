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

readCSV(path_data, data_products)
data = readCSV(path_data, data_order_prior)  
productInfo = readCSV(path_data, data_products)
productInfo   
products = printAllProductsInOrder(9, data, productInfo) #number of products : 49687
products

#------------------------------------
# for each product, get definition
#------------------------------------
from textblob import Word
from textblob.wordnet import VERB

productName = p.values[0]
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
getProductDescOfNoun(products[1])

products[3]
getFullDefinitionFromLastword(products[3])

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