#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 00:44:12 2021

@author: jaquiroz
"""

#7.5 Capitalize the element in things that refers to a person and then print
#the list. Did it change the element in the list?

things = ['mozzarella','cinderella','salmonella']
n = things.index('cinderella')
things[n] = things[n].capitalize()
print(things)