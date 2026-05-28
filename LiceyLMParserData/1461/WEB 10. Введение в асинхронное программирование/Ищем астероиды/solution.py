import asyncio
from collections import Counter
from PIL import Image


async def process_file(filename: str):
    print(f"Start {filename}")

    with Image.open(filename) as img:
        img_rgb = img.convert("RGB")
        w, h = img_rgb.width, img_rgb.height
        total_pixels = w * h
        pixels = img_rgb.getdata()
        total_bright = 0
        for r, g, b in pixels:
            total_bright += r + g + b
        avg_bright = total_bright / total_pixels
        bright_pixels = []
        pixels = list(pixels)
        for idx, (r, g, b) in enumerate(pixels):
            if r + g + b > avg_bright:
                bright_pixels.append((idx % w, idx // w, (r, g, b)))
        len_bright = len(bright_pixels)
        del pixels

    await asyncio.sleep(0.1)

    async def compute_percent():
        if not bright_pixels:
            perc = 0
        else:
            color_counts = Counter(p[2] for p in bright_pixels)
            most_common_count = color_counts.most_common(1)[0][1]
            perc = int(most_common_count / total_pixels * 1000)
        print(f"Done {filename}, percent {perc}")
        return perc

    async def compute_amount():
        amt = int(len_bright / total_pixels * 100)
        print(f"Done {filename}, amount {amt}")
        return amt

    async def compute_quarter():
        if not bright_pixels:
            q = "I"
        else:
            mid_x, mid_y = w / 2.0, h / 2.0
            cnt = {"I": 0, "II": 0, "III": 0, "IV": 0}
            for x, y, _ in bright_pixels:
                if x >= mid_x and y < mid_y:
                    cnt["I"] += 1
                elif x < mid_x and y < mid_y:
                    cnt["II"] += 1
                elif x < mid_x and y >= mid_y:
                    cnt["III"] += 1
                else:  # x >= mid_x and y >= mid_y
                    cnt["IV"] += 1
            q = max(
                cnt.keys(),
                key=lambda k: (
                    cnt[k],
                    -int(
                        k.replace("I", "1")
                        .replace("II", "2")
                        .replace("III", "3")
                        .replace("IV", "4")
                    ),
                ),
            )
        print(f"Done {filename}, quarter {q}")
        return q

    perc, amt, q = await asyncio.gather(
        compute_percent(), compute_amount(), compute_quarter()
    )
    print(f"Ready {filename}")
    return filename, perc, amt, q


async def asteroids(*filenames: str):
    return await asyncio.gather(*(process_file(f) for f in filenames))