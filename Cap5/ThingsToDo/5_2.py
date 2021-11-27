questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father´s Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

#Emparejar en una nueva lista en el orden Question y Answer
#result = questions[0]+answers[1]+questions[1]+answers[2]+questions[2]+answers[0]#Salida como String
result=[]
result.append(questions[0])
result.append(answers[1])
result.append(questions[1])
result.append(answers[2])
result.append(questions[2])
result.append(answers[0])#Salida como lista

    
print(result)
