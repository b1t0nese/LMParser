import sys
import requests

geocode = " ".join(sys.argv[1:]) if sys.argv[1:] else input("Введите адрес: ")

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
    "format": "json",
    "geocode": geocode
}
response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass
json_response = response.json()
out_data = json_response["response"]["GeoObjectCollection"]["featureMember"]
out_data = map(lambda x: x['GeoObject']['metaDataProperty']['GeocoderMetaData'], out_data)

searched_metro = None
for dat in out_data:
    if dat.get("kind") == "metro":
        print(dat["text"])
        break
else:
    print("Ничё не найдено(")