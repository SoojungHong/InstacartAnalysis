#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 15:21:30 2018

@author: soojunghong
"""
#--------------------
# import libraries 
#-------------------
import csv 
import os
import pandas as pd

#------------------
# functions 
#------------------
def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row)) 
        
def readCSV(filePath, fileName): 
    csv_path = os.path.join(filePath,fileName)
    return pd.read_csv(csv_path)        

#-------------
# read data 
#-------------
path_data = "/Users/soojunghong/Documents/safariML/ML_python/kaggle/InstacartAnalysis/data/"
data_aisle = "aisles.csv"
data_dept = "departments.csv"
data_order_prior = "order_products_prior.csv"
data_order_train = "order_products_train.csv"
data_orders = "orders.csv"
data_products = "products.csv"

readCSV(path_data, data_aisle)
readCSV(path_data, data_dept)
readCSV(path_data, data_order_prior) #order_id, product_id, add_to_cart_order, reordered
# TODO_1 : which product_id were reordered? 
readCSV(path_data, data_order_train)
readCSV(path_data, data_orders) # order_id  user_id eval_set  order_number  order_dow  order_hour_of_day  days_since_prior_order

readCSV(path_data, data_products)
readCSV(path_data, "sample_submission.csv")

#-------------------------------------------
# ToDo_1 : which product_id were reordered
#-------------------------------------------
order_prior = readCSV(path_data, data_order_train)
order_prior
reordered = order_prior.loc[order_prior['reordered'] == 1]
reordered
most_reordered_product = reordered.product_id.mode()
most_reordered_product #24852

product = readCSV(path_data, data_products)
product.loc[product['product_id'] == 24852] 

#---------------------------------------------------------------------------
# separate eval_set 'prior', 'train', 'test' from data_orders.csv 
#---------------------------------------------------------------------------
all_orders = readCSV(path_data, data_orders)
all_orders.count() #3421083

prior = all_orders.loc[all_orders['eval_set'] == 'prior'] #loc is to select rows by label
prior.count() #3214874

train = all_orders.loc[all_orders['eval_set'] == 'train']
train
train.count() #131209

test = all_orders.loc[all_orders['eval_set'] == 'test']
test
test.count() #75000

