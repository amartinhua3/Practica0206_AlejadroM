import urllib.request
url = 'http://textfiles.com/adventure/aencounter.txt'
def leer_url(url):
    file = urllib.request.urlopen(url)
    for linea in file:
        num_palabras = linea.decode('utf-8')
        print(num_palabras)
        return
leer_url(url)