# Сейчас работает вроде
import requests

server_address = 'http://geocode-maps.yandex.ru/v1/?'
api_key = '8013b162-6b42-4997-9691-77b7074026e0'
geocode = input("Введите адрес: ")
geocoder_request = f'{server_address}&apikey={api_key}&geocode={geocode}&kind=metro&results=50&format=json'
response = requests.get(geocoder_request)

json_response = response.json()

toponym = json_response["response"]["GeoObjectCollection"]["featureMember"]

for obj in toponym:
    if obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["kind"] == "metro":
        print(obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"])
        break
else:
    print("Ничего не найдено")