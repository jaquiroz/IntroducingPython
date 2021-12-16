guess_me = 5
for number in range (9): 
    if number < guess_me:
       print (number,"too low")
    elif number == guess_me:
        print ("found it!")
    elif number > guess_me:
        print("opps")
        break

    

  
    
