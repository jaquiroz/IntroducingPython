#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:05:16 2021

@author: jaquiroz
"""

#Create from String with split()
talk_like_a_pirate_day = '9/19/2019'
talk_list = talk_like_a_pirate_day.split('/')
print(talk_list)

splitme = 'a/b//c/d///e'
splitme_list = splitme.split('/')
print(splitme_list)

#Get Items with a Slice
marxes = ['Hugo','Paco','Luis']
aux1 = marxes[0:1]
aux2 = marxes[::-1]#Reverse list
print(aux1)
print(aux2)

#Add an item to the end with append()
friends = ['Mario','Yoshi','Luigui']
friends.append('Peach')
print(friends)

#Add an Item by Offset with insert()
siblings = ['Jorge','Nelson','Lizeth']
siblings.insert(2,'Nacho')
print(siblings)

#Combine List by using extend or +
store = ['potatoes','tomatoes','onion','cheese']
supply = ['pinneaple','apple']
store.extend(supply)
print(store)

#Change an intem by offset
pets = ['Coco','Nacho','Mancha']
pets[2] = 'Iori'
print(pets)

#Change Iems with a slice
numbers = [1,2,3,4]
numbers[1:3] = [5,6]
print(numbers)

example1 = [2,4,6,8]
example1[1:3]=[]
print(example1)

example2 = [1,2,3,4]
example2[1:3] = 'what?'
print(example2)

#Delete an Item by offset with del
colors = ['red','yellow','blue','black']
del colors[2]
print(colors)

#Delete with remove
names = ['Jorge','Nelson','Lizeth','Rodrigo']
names.remove('Rodrigo')
print(names)