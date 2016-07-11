#!/usr/bin/python3
from PIL import Image

if __name__ == "__main__":
    image = Image.open('fraz.jpg')
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel( (x,y) )
            image.putpixel( (x,y), (r, g+100, b))
    image.save('out.jpg')
