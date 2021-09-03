quesos = ['cheddar','mozarella','criollo']

for muestra in quesos:
    if  muestra.startswith('m'):
        print("No comere un queso que comience con 'm'")
        break
    else:
        print(muestra)