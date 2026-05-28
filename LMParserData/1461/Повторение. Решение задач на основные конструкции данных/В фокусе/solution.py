from PIL import Image, ImageChops

image = Image.open("image.png")
diffr = ImageChops.difference(image, Image.new(
    image.mode, image.size, image.getpixel((0, 0))))
image = image.crop(diffr.getbbox())
image.save("res.png")