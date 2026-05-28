import requests

point = input().split()
response = requests.post(
    "https://api.weather.yandex.ru/graphql/query",
    headers={"X-Yandex-Weather-Key": "fa0f11a5-fd86-48c2-b07f-ef6e45a933a8"},
    json={"query": f"""{{
  weatherByPoint(request: {{ lat: {point[0]}, lon: {point[1]} }}) {{
    climate {{
      months(limit: 12) {{
        avgDayTemperature
      }}
    }}
  }}
}}"""},
)
temp = [
    obj["avgDayTemperature"]
    for obj in response.json()["data"]["weatherByPoint"]["climate"]["months"]
]
minn = 0 if min(temp) >= 1 else min(temp)

print("Среднемесячные температуры:")
for i in range(0, 12):
    if temp[i] <= -1:
        print(
            " " * (abs(minn) - abs(temp[i]))
            + "*" * (abs(minn) - (abs(minn) - abs(temp[i])))
            + "|"
        )
    else:
        print(" " * abs(minn) + "|" + "*" * temp[i])