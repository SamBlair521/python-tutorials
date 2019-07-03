# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:23:54 2019

@author: Sam
"""

import requests

r = requests.get('https://raw.githubusercontent.com/becloudready/snowflake-tutorials/master/dataset/employees01.csv')

listdata3 = r.text.split('\n')

listdata3[1]

f=open('C:/Users/Sam/sam_python.txt', 'w')

f.write(listdata3[1])
f.close()
