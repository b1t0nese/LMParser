import asyncio
import sys


async def buy(gift, q):
    name, st, wt = gift
    print(f"Buy {name}")
    await asyncio.sleep(st)
    await q.put((name, wt))


async def process(stop, depart, travel, gifts, q):
    print(f"Buying gifts at {stop} stop")
    tasks = []
    time_used = 0
    for g in sorted(gifts, key=lambda x: x[1] + x[2], reverse=True)[:]:
        if time_used + g[1] <= depart:
            time_used += g[1]
            gifts.remove(g)
            t = asyncio.create_task(buy(g, q))
            tasks.append((t, g[0], g[2]))
    await asyncio.sleep(depart)
    for t, name, wt in tasks:
        await t
        await asyncio.sleep(wt)
        print(f"Got {name}")
    print(f"Arrive from {stop} stop")
    return travel


async def final(gifts, q):
    if not gifts:
        return
    print("Buying gifts after arrival")
    tasks = [asyncio.create_task(buy(g, q)) for g in gifts]
    for t, (name, _, wt) in zip(tasks, gifts):
        await t
        await asyncio.sleep(wt)
        print(f"Got {name}")


async def main():
    data = [line.strip() for line in sys.stdin if line.strip()]
    stops, gifts = [], []
    i = 0
    while i < len(data) and len(data[i].split()) == 2 and data[i].split()[0].isdigit():
        stops.append(tuple(map(int, data[i].split())))
        i += 1
    for j in range(i, len(data)):
        p = data[j].split()
        if len(p) == 3:
            gifts.append([p[0], int(p[1]) / 100, int(p[2]) / 100])
    stops = [(d / 100, t / 100) for d, t in stops]
    q = asyncio.Queue()
    for idx, (dep, travel) in enumerate(stops, 1):
        travel = await process(idx, dep, travel, gifts, q)
        if idx < len(stops):
            await asyncio.sleep(travel)
    await final(gifts, q)


if __name__ == "__main__":
    asyncio.run(main())