#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 18:20:30 2021

@author: jaquiroz
"""

#Get an item by key or with get()
some_pythons = {
    'Graham':'Chapman',
    'John':'Cleese',
    'Eric':'Idle',
    'Terry':'Gilliam',
    'Michael':'Palin',
    'Terry':'Jones',
    }

print(some_pythons['John'])
print(some_pythons.get('Eric'))
print(some_pythons.get('Grooucho','NOT a Python'))#Deja un mensaje si no encuentra el key

#Get al keys with keys()
signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
k = list(signals.keys())#List para realizar operaciones
print(signals.keys())
print(k)

#Get all calues with values()
l = list(signals.values())
print(l)

#Get all key-value pairs with items()
d = list(signals.items())#Regresa Tupple
print(d)

#Get length with len()
n = len(signals)
print(n)

#Combine dictionaries with {**a,**b}
first = {'a':'agony','b':'bliss'}
second = {'b':'bagels','c':'candy'}
aux = {**first, **second}
print(aux)
third = {'d':'donuts'}
aux2 = {**first, **third, **second}    
print(aux2)

#Combine dictionaries with update()
pythons = {
    'Chapman':'Graham',
    'Cleese':'John',
    'Gilliam':'Terry',
    'Idle':'Eric',
    'Jones':'Terry',
    'Palin':'Michael'
    }

others = {'Marx':'Groucho','Howard':'Moe'}
pythons.update(others)
print(pythons)

