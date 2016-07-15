#!/usr/bin/python3
from PIL import Image
import os

def cript(file_name):
    """docstring for cript"""
    image = Image.open(file_name)
    width, height = image.size

    key = Image.open("key.jpg")
    key_width, key_height = key.size

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel( (x,y) )
            kr, kg, kb = key.getpixel( ((x)%key_width,(y)%key_height) )
            image.putpixel( (x,y), ((r + kr)%256, (g + kg)%256, (b + kb)%256))
    image.save('out.jpg')
    output_path = os.path.abspath("out.jpg")
    return output_path
