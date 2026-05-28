import requests
adress, port, a, b = [input() for i in range(4)]
output = requests.get(f"{adress}:{port}?a={a}&b={b}").json()
print(" ".join(map(str, sorted(output["result"]))))
print(output["check"])