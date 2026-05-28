import asyncio
import time


async def interview_2(*data):
    tasks = list(map(list, zip(*[iter(data[1:])] * 2)))
    for i, d in enumerate(tasks):
        print(f"{data[0]} started the {i + 1} task.")
        await asyncio.sleep(d[0] / 100)
    for i, d in enumerate(tasks):
        print(f"{data[0]} moved on to the defense of the {i + 1} task.")
        time.sleep(d[1] / 100)
        print(f"{data[0]} completed the {i + 1} task.")


async def interviews_2(*data):
    tasks = []
    for d in data:
        tasks.append(asyncio.create_task(interview_2(*d)))
    await asyncio.gather(*tasks)