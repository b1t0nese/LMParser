import asyncio
import time


async def interview(*data):
    tasks = list(map(list, zip(*[iter(data[1:])] * 2)))
    for i, d in enumerate(tasks):
        tms = list(map(lambda x: x / 100, d + [5]))
        print(f"{data[0]} started the {i + 1} task.")
        await asyncio.sleep(tms[0])
        print(f"{data[0]} moved on to the defense of the {i + 1} task.")
        await asyncio.sleep(tms[1])
        print(f"{data[0]} completed the {i + 1} task.")
        if i + 1 < len(tasks):
            print(f"{data[0]} is resting.")
            await asyncio.sleep(tms[2])


async def interviews(*data):
    tasks = []
    for d in data:
        tasks.append(asyncio.create_task(interview(*d)))
    await asyncio.gather(*tasks)