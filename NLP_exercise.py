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