#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 01:03:40 2021

@author: jaquiroz
"""

#7.9 Lowercase the last element of the surprise list, reverse it, and then
#capitalize it.

surprise = ['Groucho','Chico','Harpo']
n=len(surprise)
surprise[n-1] = surprise[n-1].lower()
print(surprise)

surprise_invert = surprise[::-1]
surprise_invert[0] = surprise_invert[0].capitalize()
print(surprise_invert)