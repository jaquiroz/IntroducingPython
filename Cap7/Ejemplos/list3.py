#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 11:04:13 2021

@author: jaquiroz
"""
#Compare list
a = [7,2]
b = [7,2,9]
print(a==b)

#Iterate with for and in
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)
    
#Iterate and break
cheeses1 = ['brie', 'gjetost', 'havarti']
for x in cheeses1:
    if x.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
            print(x)
            
cheeses2 = ['brie', 'gjetost', 'havarti']
for x in cheeses1:
    if x.startswith('x'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
            print(x)
else:
    print("Didn't find anything that started with 'x'")
    
#Iterate multiple sequences with zip()
days = ['Monday','Tuesday','Wednesday']
fruits = ['banana','orange','peach']
drinks = ['coffee','tea','beer']
desserts = ['tiramisu','ice cream','pie','pudding']
for day,fruit,drink,dessert in zip(days,fruits,drinks,desserts):
    print(day, ": drink",drink,"- eat",fruit,"- enjoy",dessert)
    
#Create a list with a comprehension
number_list = [number for number in range(1,6)]
#number_list = [number-1 for number in range(1,6)]
print(number_list)

a_list = [numero for numero in range(1,6) if numero % 2 ==1]
print(a_list)

rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print(cell)