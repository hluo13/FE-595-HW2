#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:47:23 2020

@author: tianyiyang
"""


import requests 
from bs4 import BeautifulSoup 

with open("inputs.txt",'w') as f:
    for i in range(0,50):
        res = requests.get('http://3.95.249.159:8000/random_company')
        html = res.text
        soup = BeautifulSoup( html,'html.parser') 
        items = soup.find_all( 'li' )
        name = items[0]
        f.write(name.text)
        f.write('\n')
        for item in range(0,len(items)):
            if items[item].text[0]=='P':
                purpose = items[item]
            
                f.write(purpose.text)
                f.write('\n')
    f.close()
