song = """When a eel grabs your arm,
And it causes great harm,
Thats's - a moray!"""
#Cambiar a mayusculas las palabras con M
word = " moray"
index_m= song.index(word)
song_aux=song[index_m+1:]
song_aux_cap = song_aux.capitalize()
new_song= song[:index_m+1]+song_aux_cap
print(new_song)