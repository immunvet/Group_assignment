# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:39:13 2018

@author: Andrii Trokoz
"""
from collections import Counter
with open('./new_file.txt', 'r+') as text:
    read_text = text.read().strip().split()

    
    new_list = []
    
    for i in read_text:
            new_list.append(i.lower())
    
    print(Counter(new_list))
            
         
    
    
    
