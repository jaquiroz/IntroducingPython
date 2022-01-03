#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 17:34:05 2021

@author: jaquiroz
"""

#Create with set
empty_set = set()
print(empty_set)

even_numbers = {0,2,4,6,8}
print(even_numbers)

odd_numbers = {1,2,5,7,9}
print(odd_numbers)

#Convert with set()
example = set('letters')#String
print(example)

example2 = set(['Dasher','Dancer','Prancer','Mason_Dixon'])#List
print(example2)

example3 = set(('Ummaguma','Echoes','Atom  Heart Mother'))#Tuple
print(example3)

example4 = set({'apple':'red','orange':'orange','cherry':'red'})#Dictionary
print(example4)

#Get length with len()
reindeer = set(['Dasher','Dancer','Prancer','Mason-Dixon'])
n = len(reindeer)
print(n)

#Add an Item with add()
s = set((1,2,3))
print(s)
s.add(4)
print(s)

#Delete an item wth remove()
s.remove(3)
print(s)

n