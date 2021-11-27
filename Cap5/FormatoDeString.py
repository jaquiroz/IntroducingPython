# -*- coding: utf-8 -*-
actor = 'Chris Evans'
cat = 'Coco'
weight = '28'

#Formato para Python 2 y 3
print("My wife's favorite actor is %s" %actor )
print("Our cat %s weights %s pounds"%(cat,weight))


#Nuevo formato python 3.6
thing = 'woodchuck'
place = 'lake'
d = {'thing':'duck','place':'bathtub'}
print ('The {} is in the {}.'.format(thing, place))
print ('The {1} is in the {0}.'.format(place, thing))
print ('The {thing} is in the {place}.'.format(thing = 'duck' ,\
                                               place = 'bathtub'))
print ('The {0[thing]} is in the {0[place]}.'.format(d))

#Formato python 3.8
pet = 'cat'
room = 'bedroom'
print(f'The {pet} is in the {room}')