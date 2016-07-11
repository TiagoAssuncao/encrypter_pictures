#!/usr/bin/python3
from PIL import Image
import os

def cript(file_name):
    """docstring for cript"""
    image = Image.open(file_name)
    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel( (x,y) )
            image.putpixel( (x,y), (r - 100, g + 100, b + 50))
    image.save('out.jpg')
    output_path = os.path.abspath("out.jpg")
    return output_path
