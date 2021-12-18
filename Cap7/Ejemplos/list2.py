#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 18:40:01 2021

@author: jaquiroz
"""

#Find an item's offset by value with index
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
n1 = marxes.index('Chico')
print(n1)

#Test for a value with in
names = ['Jorge','Nelson','Lizeth','Nacho']
state = 'Nacho' in names
print(state)

#Count ocurrences of a value with count
repeat = ['Lizeth','Nelson','Pedro','Lizeth']
n2 = repeat.count('Lizeth')
print(n2)

#Convert a List to a String with join
friends = ['Harry', 'Hermione','Ron']
separator = '*'
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)

#Reorder itms with sort or sorted
Example1 = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
sorted_Example1 = sorted(Example1)#Create a copy of Example1
print(sorted_Example1)

Example2 = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
Example2.sort()
print(Example2)

Example3 = [2,1,4.0,5]
Example3.sort(reverse=True)
print(Example3)

#Get length with len()
print(len(Example3))

#Copy with copy(), list() or a slice
a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]

#Copy everything with deepcopy()
import copy
e = [1,2,[8,9]]
f = copy.deepcopy(e)
e[2][1] = 10
print(e)
print(f)