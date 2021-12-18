#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:06:56 2021

@author: jaquiroz
"""

#Tuples
marx_tuple = ('Groucho','Chico','Harpo')  #Basic form


#Tuple unpacking
a,b,c = marx_tuple

print(a)
print(b)
print(c)
#Convert to tuple
marx_list = ['Groucho','Chico','Harpo'] 
aux = tuple(marx_list)
print(aux)

#Combine tuples
A_tuple = ('Hugo',)
B_tuple = ('Paco','Luis')
C_tuple = A_tuple + B_tuple
print(C_tuple)

#Compare tupple
e = (7,2)
f = (7,2,9)
print(e==f)
print(e<=f)

#Iterate with for
words = ('fresh','out', 'of', 'ideas')
for word in words:
    print(word)
    
