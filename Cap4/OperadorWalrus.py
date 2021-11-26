# -*- coding: utf-8 -*-
#Codigo normal 
#tweet_limit = 280
#tweet_string = "BLah" * 50
#diff = tweet_limit - len(tweet_string)
#if diff >=0:
#    print("A fitting tweet")
#else:
#    print("Went ober by",abs(diff))
    
#Operador Walrus
tweet_limit = 280
tweet_string = "BLah" * 50

if diff:= tweet_limit - len(tweet_string) >=0:
    print("A fitting tweet")
else:
    print("Went ober by",abs(diff))