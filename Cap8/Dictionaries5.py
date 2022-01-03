#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 19:39:17 2021

@author: jaquiroz
"""

#Dictionary comprehensions
#{key_epression : value_expression for expression in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

letter_counts2 = {letter2: word.count(letter2) for letter2 in set(word)}
print(letter_counts2)

#If 
vowels = 'aeiou'
word2 = 'onomatopoeia'
vowels_counts = {letter3:word2.count(letter3) for letter3 in set(word2)
                 if letter3 in vowels}

print(vowels_counts)