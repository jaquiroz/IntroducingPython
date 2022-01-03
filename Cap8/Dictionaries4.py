#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 19:21:08 2021

@author: jaquiroz
"""

#Copy everything with deepcopy() [Sirve para valores mutables]
import  copy
colors = {'green':'go',
           'yellow':'go faster',
           'red':['stop','smile']
    }

colors_copy = copy.deepcopy(colors)
colors['red'][1] = 'sweat'
print(colors)
print(colors_copy)

#Compare dictionaries(No importa el orden)
a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a==b)

c = {1:[1,2], 2:[1], 3:[1]}
d = {1:[1,1], 2:[1], 3:[1]}
print(c==d)

#Iterate with for and  in
accusation = {'room':'ballroom','weapon':'lead pipe',
              'person':'Col. Mustard'}

for card in accusation:#Key iteration
    print(card)

for  value in  accusation.values():#Value iteration
    print(value)
    
for item in accusation.items():#Item iteration
    print(item)
    
for card, contents in accusation.items():
    print('Card', card, 'has the content', contents)
