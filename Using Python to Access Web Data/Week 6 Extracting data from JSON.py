#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:42:54 2021

@author: fanli
"""

import urllib.request
import json

url = input("Enter url: ")
data = urllib.request.urlopen(url).read()
dict = json.loads(data)
# check data
#print(json.dumps(dict,indent = 2))
print(sum([i['count']for i in dict["comments"]]))
