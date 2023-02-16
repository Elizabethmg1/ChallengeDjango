from urllib.request import urlopen
import json

def devolver_json(self):
    url="http://api.citybik.es/v2/networks/bikesantiago"

    response = urlopen(url)
    data = json.loads(response.read())
    return data