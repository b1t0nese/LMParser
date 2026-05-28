import csv
n_school, n_class = list(map(int, input().split()))
result = []
with open("rez.csv", "r", encoding="utf-8") as f:
    for user in csv.DictReader(f):
        login = user["login"].split("-")
        if n_school == int(login[2]) and n_class == int(login[3]):
            result.append((user["user_name"].split()[3], user["Score"]))
result.sort(key=lambda x: x[1] + x[0], reverse=True)
for user in result:
    print(*user)