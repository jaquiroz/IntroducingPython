#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 17:59:50 2021

@author: jaquiroz
"""

#Delete an item by Key with del
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
del pythons['Marx']#Borra del diccionario el contenido del key
print(pythons)
del pythons['Howard']
print(pythons)

#Delete all items with clear()
pythons.clear()
print(pythons)

#Test for a key with in
aux = {'Chapman':'Graham','Cleese':'John','Jones':'Terry',
       'Palin':'Michael','Idle':'Eric'}
state1 = 'Chapman' in aux
state2 = 'Guilliam' in aux
print(state1)
print(state2)

#Assign with = 
signals = {'green':'go',
           'yellow':'go faster',
           'red':'smile for the  camera'
    }
save_signals = signals
signals['blue']= 'confuse everyone'
print(save_signals)

#Copy with copy() [Funciona con valores inmutables]
colors = {'green':'go',
           'yellow':'go faster',
           'red':'smile for the  camera'
    }
originals_colors = colors.copy()
colors['blue'] = 'confuse everyone'
print(signals)
print(originals_colors)



