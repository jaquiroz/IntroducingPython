# -*- coding: utf-8 -*-
word = 'coquito'
for letter in word:
    if letter == 'x':
        print("ENCONTRAMOS una x")
        break
    print(letter)
    
else:
    print("NO encontramos una x")
