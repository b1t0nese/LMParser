menu = dict([input().split("\t") for _ in range(int(input()))])
input()
orders, product = [], ""
while product != ".":
    product = input()
    if not product and (orders and orders[-1]) or not orders:
        orders.append([])
    if product and product != ".":
        orders[-1 if orders else 0].append(product.split("\t"))
results = [sum(map(lambda x: int(menu[x[0]]) * int(x[1]), order)) for order in orders]
for i, result in enumerate(filter(lambda x: x, results)):
    print(f"{i + 1}) {result}")
print(f"Итого: {sum(results)}")