n = int(input())
points_on_axes = []
quarters = [0, 0, 0, 0]

for i in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        points_on_axes.append((x, y))
    else:
        if x > 0 and y > 0:
            quarters[0] += 1
        elif x < 0 and y > 0:
            quarters[1] += 1
        elif x < 0 and y < 0:
            quarters[2] += 1
        elif x > 0 and y < 0:
            quarters[3] += 1

for point in points_on_axes:
    print(f"({point[0]}, {point[1]})")

results = [f"{['I', 'II', 'III', 'IV'][i]}: {quarters[i]}" for i in range(4)]
print(", ".join(results) + ".")