import requests, json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def handle(request):
    urldolar = "https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar?apikey=4422286a2b6538121f331725568810b163fc4238&formato=json"
    resdolar = requests.get(urldolar, verify=False)
    urltemp = "https://api.openweathermap.org/data/2.5/weather?q=Santiago&units=metric&lang=es&appid=32a86e5ed5641b5c40972f4af8e0cc07"
    restemp = requests.get(urltemp)
    urluf = "https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=4422286a2b6538121f331725568810b163fc4238&formato=json"
    resuf = requests.get(urluf,verify=False)
    urlcru = "https://www.crucigrama.org/index.php?groupid=Nivel+2+medio%3A+Definiciones&Submit=Generar+nuevo&max_words=10&ActivarSopa=0&cols=15&rows=15"
    temp = (restemp.json())['main']['temp']
    if resdolar.status_code == 404:
        dolar = "El valor del dolar no ha sido actualizado"
    else:
        dolar = (resdolar.json())['Dolares']
    uf = resuf.json()['UFs']
    cru = urlcru
    resp = ("Temperatura: ", temp, "C", "Dolar: ", dolar, "UF: ", uf, "Crucigrama: ", cru)
    return resp


