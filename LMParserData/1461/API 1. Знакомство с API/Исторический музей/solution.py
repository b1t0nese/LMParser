import requests

server_address = 'http://geocode-maps.yandex.ru/1.x/?'
api_key = '8013b162-6b42-4997-9691-77b7074026e0'
geocode = 'Красная площадь, 1, Москва, Исторический музей'
geocoder_request = f'{server_address}apikey={api_key}&geocode={geocode}&format=json'

response = requests.get(geocoder_request)
if response:
    json_response = response.json()

    # Согласно описанию ответа, он находится по следующему пути:
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Полный адрес топонима:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Печатаем извлечённые из ответа поля:
    print(toponym_address, "имеет координаты:", toponym_coodrinates)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")