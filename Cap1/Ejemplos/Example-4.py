import webbrowser
import json
from urllib.request import urlopen

print("Vamos a encontrar una pagina web antigua:")
site = input("Ingrese una direccion URL:")
era = input("Ingrerse un año, mes y dia, en el formato 20150613:")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)#Conecta al sevidor para realizar la busqueda 
contents = response.read()#Recibimos los resultados de la busqueda
text = contents.decode("utf-8")#Decodificamos la informacion recibida en un archivo JSON
data = json.loads(text)#Convertimos el tecto en informacion
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ",old_site)
    print("La pagina deberia aparecer en tu buscador ahora.")
    webbrowser.open(old_site)
except:
    print("Lo siento, no pudimos encontrar la pagina",site)