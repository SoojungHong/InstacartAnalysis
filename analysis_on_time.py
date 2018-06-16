#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:09:34 2018

@author: soojunghong

purchasing time analysis 
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
    
     
def getProductsInfoInOrder(orderID, data, productInfo, product_dept) :
    #data = readCSV(path_data, data_order_prior)  
    #productInfo = readCSV(path_data, data_products)
    order = data[data['order_id'] == orderID] 
    prodList = []
    if(order.empty) : 
        print("There is no order in this data set")
        prodList.append("")
    prodList.append(order['product_id'].tolist())
    return prodList

    
def printAllProductsInfoInOrder(orderID, data, productInfo, product_dept) :
    #data = readCSV(path_data, data_order_prior)  
    #productInfo = readCSV(path_data, data_products)
    order = data[data['order_id'] == orderID] 
    if(order.empty) : 
        print("There is no order in this data set")
    prodList = order['product_id'].tolist()
    for ord in prodList : 
        #print(productInfo[productInfo["product_id"] == ord].product_name)
        print(product_dept[product_dept["product_id"] == ord])
   

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

readCSV(path_data, data_aisle) #133
readCSV(path_data, data_dept) #20
readCSV(path_data, data_order_prior) #order_id, product_id, add_to_cart_order, reordered
 
readCSV(path_data, data_order_train)
readCSV(path_data, data_orders) # order_id  user_id eval_set  order_number  order_dow  order_hour_of_day  days_since_prior_order

readCSV(path_data, data_products)
readCSV(path_data, "sample_submission.csv")

#-----------------------------------------------------
# which day in a week, which hour and buying what?
#-----------------------------------------------------
#get all order_id of user (example userID is 1 and get all orders)
orders = readCSV(path_data, data_orders)
orders
product = readCSV(path_data, data_products)
product
data = readCSV(path_data, data_order_prior)  
productInfo = readCSV(path_data, data_products) 
dept = readCSV(path_data, data_dept)
product_dept = productInfo.merge(dept, on='department_id', how='inner')  

user_products_id = []
ordersPerUser = orders[orders["user_id"] == 1] #userID]
ordersPerUser

# print products in one order (example, 2539329 )
print(ordersPerUser['order_dow'])
order_dow = ordersPerUser['order_dow']
order_dow
print(ordersPerUser['order_hour_of_day'])
order_hour = ordersPerUser['order_hour_of_day']
order_hour

printAllProductsInfoInOrder(431534, data, productInfo, product_dept) 

# get all products in all orders of given user (example, get all products info from user 1)
for ordr in ordersPerUser.order_id : 
    print(ordr)
    printAllProductsInfoInOrder(ordr, data, productInfo, product_dept) 
    

    
#-------------------------------------------------
# plotting about order_dow and order_hour_of_day
#-------------------------------------------------
# show the order_dow as histogram 
showHistogram(order_dow, 0, 6, 0, 10)
#show the order_hour_of_day 
showHistogram(order_hour, 0, 25, 0, 10)


#ToDo : 
#--------------------------------------------------------------------
# Find out when is the most frequent customer shoppting day in week
#--------------------------------------------------------------------



#---------------------------------------------------------------------
# Find out which hour is the most frequent hour customer do shopping
#---------------------------------------------------------------------



#------------------------------------------------------------------------
# Cluster product type per day in week, i.e. which day usually buy what
#------------------------------------------------------------------------


#---------------------------------------------------------
# Cluster product per hour, i.e. which hour buying what 
#---------------------------------------------------------