# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:56:02 2017

@author: a613274
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
print(aisles_data.head())

dept_data = readCSV(DATA_PATH, DEPARTMENT_FILE)
print(dept_data.head())

order_prior = readCSV(DATA_PATH, ORDER_PRIOR_FILE)
print(order_prior) #32434488

order_train = readCSV(DATA_PATH, ORDER_TRAIN_FILE)
print(order_train) #1384617

orders_data = readCSV(DATA_PATH, ORDERS_FILE)
print(orders_data.info()) #3421083
