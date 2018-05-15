from PIL import ImageFont, ImageDraw, Image
import cv2

font_dest = '../fonts/hard.ttf'
font = ImageFont.truetype(font_dest, size=1000, index=0)

content = '   KEEP CALM\nAND CONQURE'

import matplotlib.pyplot as plt

blank = Image.new("RGB", [9300, 3000], 'black')
drawObject = ImageDraw.Draw(blank)
drawObject.text([150, 450], content, font=font)

blank.save("output1.png", "PNG")
