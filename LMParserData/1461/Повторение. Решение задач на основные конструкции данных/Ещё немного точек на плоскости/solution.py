n = int(input())
selected_points, all_points = [], []
left_point, right_point = None, None
top_point, bottom_point = None, None

for i in range(n):
    x, y = map(int, input().split())
    all_points.append((x, y))
    if abs(x) > abs(y):
        selected_points.append((x, y))

for i, (x, y) in enumerate(all_points):
    if left_point is None or x < left_point[0]:
        left_point = (x, y)
    if right_point is None or x > right_point[0]:
        right_point = (x, y)
    if top_point is None or y > top_point[1]:
        top_point = (x, y)
    if bottom_point is None or y < bottom_point[1]:
        bottom_point = (x, y)

for point in selected_points:
    print(f"({point[0]}, {point[1]})")
print(f"left: ({left_point[0]}, {left_point[1]})")
print(f"right: ({right_point[0]}, {right_point[1]})")
print(f"top: ({top_point[0]}, {top_point[1]})")
print(f"bottom: ({bottom_point[0]}, {bottom_point[1]})")