#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 17:13:32 2021

@author: jaquiroz
"""
bierce = {
    "day" :"A period of twenty-four hours, mostly misspent",
    "positive":"Mistaken at the top of one's voice",
    "misfortune":"The kind of fortune that never misses",
    }
print(bierce)
 
#dict() funtion
acme_customer = {'first':'Wile','middle':'E','last':'Coyote'}
acme_better = dict(first='Wile',middle='E',last='Coyote')
print(acme_customer)
print(acme_better)

#Convert with dict()
lol = [['a','b'],['c','d'],['e','f']]#List
lol_dict = dict(lol)
print(lol_dict)

tol = (['a','b'],['c','d'],['e','f'])#Tupple
tol_dict = dict(tol)
print(tol_dict)

los = ['ab','cd','ed']
los_dict = dict(los)
print(los_dict)

tos = ('ab','cd','ef')
tos_dict = dict(tos)
print(tos_dict)

# Add or change an itme by [key]
pythons = {
    'Chapman':'Graham',
    'Cleese':'John',
    'Idle':'Eric',
    'Jones':'Terry',
    'Palin':'Michael',
    }
print(pythons)

pythons['Guilliam'] = 'Gerry'#Add
print(pythons)

pythons['Guilliam'] = 'Terry'#Modify
print(pythons)