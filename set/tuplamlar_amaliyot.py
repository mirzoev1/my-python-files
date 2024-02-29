# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 16:17:24 2024

@author: Shukurullo
"""
#1
colors = {'red','yellow','white'}
colors.add('black')

colors.update(['green','blue'])
print(colors)

#2
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
set3 = set1&set2
print(set3)

#3
print(set1-set2)
print(set1.difference(set2))
print(set1^set2)














