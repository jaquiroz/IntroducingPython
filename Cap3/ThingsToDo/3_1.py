# -*- coding: utf-8 -*-
#3.1 How many seconds are in an hour? Use the interactive interpreter as a
#calculator and multiply the number of seconds in a minute ( 60 ) by the
#number of minutes in an hour (also 60 ).

hours = int (input("Ingrese las horas:"))
seconds = 3600 * hours
seconds_str  = str(seconds)
print("La hora en segundos es: "+seconds_str)