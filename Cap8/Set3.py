#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 20:11:27 2021

@author: jaquiroz
"""

#Set comprehensions
#{expression for expression in iterable}
#{expression for exoression in iterable if condition}
a_set = {number for number in range(1,6) if number % 3 ==1}
print(a_set)

#Create an inmutable set with frozenset()
fs = frozenset([3,2,1])
print(fs)
