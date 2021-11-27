# -*- coding: utf-8 -*-
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

lenght = len(poem) 
word = 'the'
quest_start = poem.find(word)
quest_end = poem.rfind(word)

print(lenght)
print(poem.startswith('All'))
print(poem.endswith('no'))
print(quest_start)
print(quest_end)