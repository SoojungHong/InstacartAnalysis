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

#for each product, get definition
from textblob import Word
from textblob.wordnet import VERB
word = Word("octopus")
word.synsets
Word("hack").get_synsets(pos=VERB)
Word("octopus").definitions

p = products[0]
p
p.values[0]
p.values[0]
word1 = Word(p.values[0])
word1.definitions

#get last word in product_name
product_name = TextBlob(word1)
type(product_name.words)
len(product_name.words)
product_name.words[1]
word2 = Word(product_name.words[2])
word2.definitions

def getFullDefinition(product_name):
    word1 = product_name.values[0]
    product_name = TextBlob(word1)
    #wordsLeng = len(product_name.words)
    for subPro in product_name.words :
        print(Word(subPro).definitions)

products[1]    
getFullDefinition(products[1])    

def getFullDefinitionFromLastword(product_name):
    word1 = product_name.values[0]
    product_name = TextBlob(word1)
    wordsLeng = len(product_name.words)
    print(Word(product_name.words[wordsLeng-1]).definitions)

products[2]
getFullDefinitionFromLastword(products[2])
