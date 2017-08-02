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

#order_products__prior.csv contains previous order contents for all customers. 'reordered' indicates that the customer has a previous order that contains the product.
order_prior = readCSV(DATA_PATH, ORDER_PRIOR_FILE) #order_id, product_id, add_to_cart_order, reordered
#print(order_prior) #32434488

order_train = readCSV(DATA_PATH, ORDER_TRAIN_FILE) #order_id, product_id, add_to_cart_order, reordered
#print(order_train) #1384617

#This file tells to which set (prior, train, test) an order belongs. You are predicting reordered items only for the test set orders. 'order_dow' is the day of week.
orders_data = readCSV(DATA_PATH, ORDERS_FILE) #order_id, user_id, eval_set, order_number, order_dow, order_hour_of_day, days_since_prior_order
#print(orders_data.info()) #3421083
#print(orders_data)

#ToDo : divide orders_data using eval_set as 'prior', 'train', 'test' 
#print(len(orders_data))

orders_test_data = orders_data.loc[orders_data['eval_set'] == 'test'] #75000
#print(orders_test_data)

orders_train_data = orders_data.loc[orders_data['eval_set'] == 'train'] #131209
#print(orders_train_data)

orders_prior_data = orders_data.loc[orders_data['eval_set'] == 'prior'] #3214874
print(orders_prior_data)
