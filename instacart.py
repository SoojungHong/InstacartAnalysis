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
   

def printOrderedProduct(productID) : 
    order = data_order_train[data_order_train['order_id'] == productID]
    for id in order['product_id']:
        print(id)
        print(product.loc[product['product_id'] == id])

     
def printAllProductsInOrder(orderID, data, productInfo) :
    #data = readCSV(path_data, data_order_prior)  
    #productInfo = readCSV(path_data, data_products)
    order = data[data['order_id'] == orderID] 
    if(order.empty) : 
        print("There is no order in this data set")
    prodList = order['product_id'].tolist()
    for ord in prodList : 
        print(productInfo[productInfo["product_id"] == ord].product_name)

     
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
   
     
def getProductsInfoInOrder(orderID, data, productInfo, product_dept) :
    #data = readCSV(path_data, data_order_prior)  
    #productInfo = readCSV(path_data, data_products)
    order = data[data['order_id'] == orderID] 
    if(order.empty) : 
        print("There is no order in this data set")
    prodList = order['product_id'].tolist()
    return prodList

   

def mostFrequentlyPurchasedByUser(userID) : 
    user_products_id = []
    ordersPerUser = orders[orders["user_id"] == userID]
    for ordr in ordersPerUser.order_id : 
        #print(ordr)
        currlist = getProductsInfoInOrder(ordr, data, productInfo, product_dept)
        for p in currlist : 
            #print(product[product["product_id"] == p].product_name)  
            user_products_id.append(p)
    
    c = Counter(user_products_id)
    mostfreq_id = c.most_common(1)
    mostfreq =product.loc[product['product_id'] == mostfreq_id[0][0]] 
    return mostfreq

    
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
 
readCSV(path_data, data_order_train)
readCSV(path_data, data_orders) # order_id  user_id eval_set  order_number  order_dow  order_hour_of_day  days_since_prior_order

readCSV(path_data, data_products)
readCSV(path_data, "sample_submission.csv")

#-------------------------------------------
# which product_id were reordered
#-------------------------------------------
order_train = readCSV(path_data, data_order_train)
order_train

reordered = order_train.loc[order_train['reordered'] == 1]
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
prior.sort_values(by = 'order_id', ascending=True)

train = all_orders.loc[all_orders['eval_set'] == 'train']
train
train.count() #131209

test = all_orders.loc[all_orders['eval_set'] == 'test']
test
test.count() #75000
test.sort_values(by = 'order_id', ascending=True)

#---------------------------------
# sort data_orders with order_id 
#---------------------------------
sorted_all_orders = all_orders.sort_values(by = 'order_id', ascending=True)
sorted_all_orders


#----------------------------------
# print product info in one order
#----------------------------------
order_1 = data_order_train[data_order_train['order_id'] == 1] #36, 38

for id in order_1['product_id']:
    print(id)
    print(product.loc[product['product_id'] == id]) 
    
        

printOrderedProduct(36)  

printOrderedProduct(38) 


#---------------------------------------------------------------
# analyse 'data_order_prior' : which products are in one order
#--------------------------------------------------------------- 
data = readCSV(path_data, data_order_prior)  
order = data[data['order_id'] == 2] 
type(order)
productInfo = readCSV(path_data, data_products)
productInfo
#get product_id as list
prodList = order['product_id'].tolist()
#for each product_id in the list print what it is 
prodList
for ord in prodList : 
    print(productInfo[productInfo["product_id"] == ord].product_name)

# print product info in an order    
data = readCSV(path_data, data_order_prior)  
productInfo = readCSV(path_data, data_products)
productInfo   
printAllProductsInOrder(9, data, productInfo) #number of products : 49687


#------------------------------------------------------
# product and its department : join product and dept 
#------------------------------------------------------
dept = readCSV(path_data, data_dept)
product_dept = productInfo.merge(dept, on='department_id', how='inner')
product_dept[product_dept["product_id"] == 1]

   
printAllProductsInfoInOrder(6, data, productInfo, product_dept)

#---------------------
# get orders by user 
#---------------------
orders = readCSV(path_data, data_orders)
ordersPerUser = orders[orders["user_id"] == 1]
type(ordersPerUser.order_id)

for ord in ordersPerUser.order_id : 
    printAllProductsInfoInOrder(ord, data, productInfo, product_dept)
    print("")

# most frequently ordered product and department
ordersPerUser = orders[orders["user_id"] == 3]
ordersPerUser.order_id    
 
for ord_1 in ordersPerUser.order_id : 
    print(ord_1)
    printAllProductsInfoInOrder(ord_1, data, productInfo, product_dept)
 
user_products = []
for ord_1 in ordersPerUser.order_id : 
    print(ord_1)
    list = getProductsInfoInOrder(ord_1, data, productInfo, product_dept)
    for p in list : 
        #print(product[product["product_id"] == p].product_name)  
        user_products.append(product[product["product_id"] == p].product_name)
    
type(user_products)
user_products

#------------------------------------
# most frequently purchased product
#------------------------------------
user_products_id = []
for ord_1 in ordersPerUser.order_id : 
    print(ord_1)
    list = getProductsInfoInOrder(ord_1, data, productInfo, product_dept)
    for p in list : 
        #print(product[product["product_id"] == p].product_name)  
        user_products_id.append(p)
        
user_products_id 

from collections import Counter

c = Counter(user_products_id)
c.most_common(1)
product.loc[product['product_id'] == 39190]

mostFrequentlyPurchasedByUser(5)


#----------------------------------------------------------
# For given order, list product list and department list 
#----------------------------------------------------------
def getProductAndDept(orderId) : 
    dop = readCSV(path_data, data_order_prior)
    aisle = readCSV(path_data, data_aisle)
    dept = readCSV(path_data, data_dept)    
    order_given = dop[dop['order_id'] == orderId]
    products_in_order = order_given['product_id']

    product_info = readCSV(path_data, data_products)
    product_info

    # join : products and data_aisle and data_dept
    pro_ais = pd.merge(product_info, aisle, on='aisle_id')
    pro_dep = pd.merge(product_info, dept, on='department_id')

    pro_location = pd.merge(pro_ais, pro_dep, on='product_id')
    pro_location

    pro_location['product_name_y']

    product_list = []
    depart_list = []

    for prod in products_in_order : 
        print(pro_location[pro_location['product_id'] == prod].product_name_y)
        pName = pro_location[pro_location['product_id'] == prod].product_name_y
        product_list.append(pName)
        print(pro_location[pro_location['product_id'] == prod].department)
        depName = pro_location[pro_location['product_id'] == prod].department
        depart_list.append(depName)
    
    print(product_list)
    print(depart_list)   
    

getProductAndDept(10)


# idea 1 : I need NLP package to know the relationship between products in one order
# idea 2 : I need to know the relationship of ordered product and it's ordered time - is it correlated or not? 
# idea 3 : customer's preference? 
# idea 4 : is there any machine learning algorithm for that? 
# idea 5 : association with each department : there is often related department is order