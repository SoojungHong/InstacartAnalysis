# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:56:02 2017

@author: a613274

@question 
1. where is test data? 
2. what exactly want to predict? 
3. how to make test dataset? 
"""

import os
import pandas as pd
import numpy as np


#-----------------------------------------
# readCSV
# Parameter : directory(path), filename
#-----------------------------------------
def readCSV(filePath, fileName): 
    csv_path = os.path.join(filePath,fileName)
    return pd.read_csv(csv_path)

#---------------
# Load Data 
#---------------
DATA_PATH = "C:/Users/a613274/Kaggle/InstacartAnalysis/data"
AISLES_FILE = "aisles.csv"
DEPARTMENT_FILE = "departments.csv"
ORDER_PRIOR_FILE = "order_products__prior.csv"
ORDER_TRAIN_FILE = "order_products__train.csv"
ORDERS_FILE = "orders.csv"
PRODUCT_FILE = "products.csv"


"""
aisles_path = os.path.join(DATA_PATH, AISLES_FILE)
print(aisles_path)
aisles_data = open(aisles_path, 'rb')
aisles = pd.read_csv(aisles_data)
print(aisles.head())
aisles.info()
"""

aisles_data = readCSV(DATA_PATH, AISLES_FILE)
#print(aisles_data)

dept_data = readCSV(DATA_PATH, DEPARTMENT_FILE)
#print(dept_data)

product_data = readCSV(DATA_PATH, PRODUCT_FILE)
print(product_data)

#order_products__prior.csv contains previous order contents for all customers. 'reordered' indicates that the customer has a previous order that contains the product.
order_prior = readCSV(DATA_PATH, ORDER_PRIOR_FILE) #order_id, product_id, add_to_cart_order, reordered
print(order_prior) #32434488

order_train = readCSV(DATA_PATH, ORDER_TRAIN_FILE) #order_id, product_id, add_to_cart_order, reordered
#print(order_train) #1384617

#This file tells to which set (prior, train, test) an order belongs. You are predicting reordered items only for the test set orders. 'order_dow' is the day of week.
orders_data = readCSV(DATA_PATH, ORDERS_FILE) #order_id, user_id, eval_set, order_number, order_dow, order_hour_of_day, days_since_prior_order
print(orders_data.info()) #3421083
print(orders_data.head())

#ToDo : divide orders_data using eval_set as 'prior', 'train', 'test' 
#print(len(orders_data))

orders_test_data = orders_data.loc[orders_data['eval_set'] == 'test'] #75000
print(orders_test_data)

orders_train_data = orders_data.loc[orders_data['eval_set'] == 'train'] #131209
print(orders_train_data)

orders_prior_data = orders_data.loc[orders_data['eval_set'] == 'prior'] #3214874
print(orders_prior_data)


#---------------------------------------
# join data frame for prior and train
#---------------------------------------
pd.merge(order_prior, orders_prior_data, on='order_id', how='inner')

pd.merge(order_train, orders_train_data, on='order_id', how='inner')

"""
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data, columns = ['subject_id','test_id'])
df_n
"""
#create dataframe of order_test 
raw_order_test = {'order_id': [np.nan], 'product_id': [np.nan], 'add_to_cart_order': [np.nan], 'reordered': [np.nan] }
order_test = pd.DataFrame(raw_order_test, columns = ['order_id', 'product_id', 'add_to_cart_order', 'reordered' ])
print(order_test)
pd.concat([order_test, orders_test_data], axis=1) #horizontally concatenate
pd.merge(order_test, orders_test_data, on='order_id', how='outer')