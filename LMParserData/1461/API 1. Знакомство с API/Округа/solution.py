import requests

def get_federal_district(city):
    api_key = "8013b162-6b42-4997-9691-77b7074026e0"
    base_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {"apikey": api_key, "geocode": city, "format": "json", "results": 1, "kind": "locality"}
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    features = response.json().get("response", {}).get("GeoObjectCollection", {}).get("featureMember", [])
    geo_object = features[0]["GeoObject"]
    address_components = geo_object.get("metaDataProperty", {}).get("GeocoderMetaData", {}).get("Address", {}).get("Components", [])
    
    for component in address_components:
        if component.get("kind") == "province":
            return component.get("name", "")

for city in ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]:
    district = get_federal_district(city)
    print(f"{city}: {district}")
