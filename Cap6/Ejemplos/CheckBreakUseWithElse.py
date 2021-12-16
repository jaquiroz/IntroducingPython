numbers =[1,2,3,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Numero encontrado",number)
        break
    position +=1
    
else:#Funciona en conjuncion de while sin utilizar el break
    print("Numero no encontrado")