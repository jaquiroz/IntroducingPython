while True:
    value = input("Entero, por favor [q para salir]:")
    if value == "q":
        break
    numero = int (value)
    if numero % 2 == 0:
        continue
    print(numero,"el cuadrado es",numero*numero)