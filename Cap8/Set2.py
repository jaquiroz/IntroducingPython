#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 17:57:30 2021

@author: jaquiroz
"""

#Iterate with for and in
furniture = set(('sofa','ottoman','table'))
for piece in furniture:
    print(piece)
    
#Test for a Value with in
drinks = {
    'martini':{'vodka','vermouth'},
    'black russian':{'vodka','kahlua'},
    'white russian':{'cream','kahlua','vodka'},
    'manhattam':{'rye','vermouth','bitters'},
    'screwdriver':{'orange juice','vodka'}
    }

for name,contents in drinks.items():
    if 'vodka' in contents:
        print(name)
        
for name,contents in drinks.items():
    if "vodka" in contents and not ('vermout' in contents or
                                    'cream' in contents):
        print(name)
        
#Combinations and operators
for name, contents in drinks.items():
    if contents & {'vermouth','orange juice'}:
        print("\n",name)
        
a = {1,2}
b = {2,3}

interseccion1 = a & b
print(interseccion1)
interseccion2 = a.intersection(b)
print(interseccion2)

union1 = a | b
print(union1)
union2 = a.union(b)
print(union2)

diferencia1 = a - b
print(diferencia1)
diferencia2 = a.difference(b)
print(diferencia2)
    
diferencia_simetrica1 = a ^ b
print(diferencia_simetrica1)
diferencia_simetrica2 = a.symmetric_difference(b)
print(diferencia_simetrica2)

#Subset
subset1 = a<=b
print(subset1)
subset2 = a.issubset(b)
print(subset2)