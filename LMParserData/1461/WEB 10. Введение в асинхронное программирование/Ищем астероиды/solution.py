import asyncio
import math
from collections import Counter
from PIL import Image
import os


async def asteroids(*files):
    tasks = [asyncio.create_task(process_image(file)) for file in files]
    results = await asyncio.gather(*tasks)
    return results


async def process_image(filename):
    print(f"Start {filename}")
    
    img = Image.open(filename)
    width, height = img.size
    total_pixels = width * height
    
    await asyncio.sleep(0.1)
    
    brightness_sum = 0
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            if isinstance(pixel, int):
                brightness = pixel
            else:
                brightness = sum(pixel[:3])
            brightness_sum += brightness
    
    avg_brightness = brightness_sum / total_pixels
    
    bright_count = 0
    bright_brightnesses = []
    quarter_counts = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
    center_x = width / 2
    center_y = height / 2
    
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            
            if isinstance(pixel, int):
                brightness = pixel
            else:
                brightness = sum(pixel[:3])
            
            if brightness > avg_brightness:
                bright_count += 1
                bright_brightnesses.append(brightness)
                
                if x >= center_x and y < center_y:
                    quarter_counts['I'] += 1
                elif x < center_x and y < center_y:
                    quarter_counts['II'] += 1
                elif x < center_x and y >= center_y:
                    quarter_counts['III'] += 1
                else:
                    quarter_counts['IV'] += 1
    
    img.close()
    
    amount = math.floor((bright_count * 100) / total_pixels) if total_pixels > 0 else 0
    
    if bright_count > 0 and bright_brightnesses:
        freq = Counter(bright_brightnesses)
        most_common_count = freq.most_common(1)[0][1]
        percent = math.floor((most_common_count * 1000) / bright_count)
    else:
        percent = 0
    
    best_quarter = 'I'
    max_count = quarter_counts['I']
    for q in ['II', 'III', 'IV']:
        if quarter_counts[q] > max_count:
            max_count = quarter_counts[q]
            best_quarter = q

    print(f"Done {filename}, percent {percent}")
    print(f"Done {filename}, amount {amount}")
    print(f"Done {filename}, quarter {best_quarter}")
    print(f"Ready {filename}")
    
    return (filename, percent, amount, best_quarter)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    test_files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
    result = asyncio.run(asteroids(*test_files))
    print(result)