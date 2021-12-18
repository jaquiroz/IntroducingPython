#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 00:50:19 2021

@author: jaquiroz
"""

#7.6 Make the cheesy element of things all uppercase and then print the list.
things = ['mozzarella','cinderella','salmonella']
n = things.index('cinderella')
things[n] = things[n].upper()
print(things)