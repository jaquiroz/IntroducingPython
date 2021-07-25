#Elige un numero entre el 1 y 10
secret = 6
#Elige otro numero entre 1 y 10
guess = 6
#Condiciones
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just righ")