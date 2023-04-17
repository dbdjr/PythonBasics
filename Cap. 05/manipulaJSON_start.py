# 
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request  
import json

def manipula():
    ende = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson"
    webUrl= urllib.request.urlopen(ende)
    if (webUrl.getcode() ==200):
        dados = webUrl.read()
        eJson = json.loads(dados)

        contagem = eJson["metadata"]["count"]
        print("Contagem: "+ str(contagem))

        for local in eJson["features"]:
            if local["properties"]["place"] == "231 km WSW of Kavieng, Papua New Guinea":
                print("****Chave especial encontrada!!!****")
            print(local["properties"]["place"])


manipula()