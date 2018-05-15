from PIL import ImageFont, ImageDraw, Image
import cv2

name_read = open('../names/name_17.txt')
name_tmp = [x[:-1] for x in name_read]

mat_size = {3: [1800, 640], 2:[1800, 640]}
start_size = {3: [150, 60], 2:[400, 60]}

font_dest = '../fonts/hard.ttf'
font = ImageFont.truetype(font_dest, size=500, index=0)

tag = 0
for content in name_tmp:
    
    tag += 1

    if len(content) not in [2, 3]:
        continue
    
    print(content)
    blank = Image.new("RGB", mat_size[len(content)], 'black')
    drawObject = ImageDraw.Draw(blank)
    drawObject.text(start_size[len(content)], content, font=font)
    blank.save("./names_pics/{}-{}.png".format(len(content), tag), "PNG")
