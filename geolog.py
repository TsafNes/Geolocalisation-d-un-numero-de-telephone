                        ########################################################################################
                        #       https://github.com/TsafNes   Copyright (C) Mai 2024     Nestor TSAFACK         #
                        ########################################################################################
"""

Ce projet permet de localiser avec exactitude la position geographique d'un numero de telephone.

"""

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Trouver le pays
num = "+14382258649"
monNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monNum, "fr")

print(localisation)

#Trouver l'operateur mobile
operateur = phonenumbers.parse(num)

print(carrier.name_for_number(operateur, "fr"))

#Trouver la latitude et la longitude
clef = "892e95d7605a4d4f8828d92b07b0871f"
coord = OpenCageGeocode(clef)
requette = str(localisation)
reponse = coord.geocode(requette)

print(reponse)

lat = reponse[0]["geometry"]["lat"]
lng = reponse[0]["geometry"]["lng"]

print(lat, lng)

#Creation de la map et localisation exacte
monMap = folium.Map(location=[lat,lng], zoom_star=12)
folium.Marker([lat,lng], popup=localisation).add_to(monMap)
monMap.save("map.html")
