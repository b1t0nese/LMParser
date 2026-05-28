import math
import requests


def get_cords(place):
    response = requests.get('http://geocode-maps.yandex.ru/1.x/?', {
        'apikey': '8013b162-6b42-4997-9691-77b7074026e0', 'geocode': place, 'format': 'json'})
    toponym = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    return toponym["Point"]["pos"]


def calc_distance(a, b):
    radians_lattitude = math.radians((a[1] + b[1]) / 2.)
    dx = abs(a[0] - b[0]) * math.cos(radians_lattitude) * 111000
    dy = abs(a[1] - b[1]) * 111000
    return math.sqrt(dx * dx + dy * dy)


a = list(map(float, get_cords("г. Москва, Останкинская телебашня").split()))
b = list(map(float, get_cords(input("Введите адрес населенного пункта: ")).split()))
antenna = round(((calc_distance(a, b) / 1000 / 3.6) - (525 ** 0.5)) ** 2)
print(f"Высота приемной антены: {antenna}м")