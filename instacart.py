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
readCSV(path_data, data_order_prior)
# TODO : which product_id were reordered? 

readCSV(path_data, data_order_train)
readCSV(path_data, data_orders)
# TODO : what is difference between 'train' and 'prior', is there overrap? 
# TODO : separate data_orders per eval_sets 

readCSV(path_data, data_products)
readCSV(path_data, "sample_submission.csv")





