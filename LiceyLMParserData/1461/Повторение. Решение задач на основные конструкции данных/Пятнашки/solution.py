from PIL import Image
from os import remove

main_image = Image.open("image.bmp")
parts_width, parts_height = main_image.width // 4, main_image.height // 4

for i in range(4):
    for j in range(4):
        new_image_filename = f"image{i + 1}{j + 1}.bmp"
        start_x, start_y = parts_width * j, parts_height * i
        sizes = (start_x, start_y, start_x + parts_width, start_y + parts_height)
        new_image = main_image.copy().crop(sizes)
        new_image.save(new_image_filename)

remove(new_image_filename)