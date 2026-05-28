import asyncio


async def grow_plant(name, soak_time, grow_time, adapt_time):
    print(f"0 Beginning of sowing the {name} plant")
    print(f"1 Soaking of the {name} started")
    fertilizers_task = asyncio.create_task(fertilizers(name))
    treatments_task = asyncio.create_task(treatments(name))

    await asyncio.sleep(soak_time / 1000)
    print(f"2 Soaking of the {name} is finished")
    print(f"3 Shelter of the {name} is supplied")

    await asyncio.sleep(grow_time / 1000)
    print(f"4 Shelter of the {name} is removed")
    print(f"5 The {name} has been transplanted")

    await asyncio.sleep(adapt_time / 1000)
    print(f"6 The {name} has taken root")

    await fertilizers_task
    await treatments_task
    print(f"9 The seedlings of the {name} are ready")


async def fertilizers(name):
    await asyncio.sleep(0.005)
    print(f"7 Application of fertilizers for {name}")
    await asyncio.sleep(0.003)
    print(f"7 Fertilizers for the {name} have been introduced")


async def treatments(name):
    await asyncio.sleep(0.005)
    print(f"8 Treatment of {name} from pests")
    await asyncio.sleep(0.005)
    print(f"8 The {name} is treated from pests")


async def sowing(*plants):
    await asyncio.gather(
        *[asyncio.create_task(grow_plant(name, soak, grow, adapt))
          for name, soak, grow, adapt in plants])