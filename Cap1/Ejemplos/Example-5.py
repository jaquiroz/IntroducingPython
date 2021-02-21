import webbrowser
import requests

print("Vamos a encontrar una pagina web antigua:")
site = input("Ingrese una direccion URL:")
era = input("Ingrerse un año, mes y dia, en el formato 20150613:")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ",old_site)
    print("La pagina deberia aparecer en tu buscador ahora.")
    webbrowser.open(old_site)
except:
    print("Lo siento, no pudimos encontrar la pagina",site)