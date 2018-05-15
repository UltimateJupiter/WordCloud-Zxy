import cv2
from matplotlib import pyplot as plt
from wordcloud import WordCloud

img_dest = 'keepcalm_box.png'
img_dest = 'black.jpg'

img_base = cv2.imread(img_dest)
img_base = cv2.cvtColor(img_base, cv2.COLOR_BGR2GRAY)
_, img_base = cv2.threshold(img_base, 200, 255, cv2.THRESH_BINARY)

#cv2.imshow('a', img_base)
#cv2.waitKey()

names = ['习近平 ', '李克强 ', '栗战书 ', '汪洋 ', '王沪宁 ', '赵乐际 ', '韩正 ', '丁薛祥 ', '王晨 ', '刘鹤 ', '许其亮 ', '孙春兰 ', '李希 ', '李强 ', '李鸿忠 ', '杨洁篪 ', '杨晓渡 ', '张又侠 ', '陈希 ', '陈全国 ', '陈敏尔 ', '胡春华 ', '郭声琨 ', '黄坤明 ', '蔡奇 ']

for x in range(6):
    names.extend(names)
    
name_co = ''.join(names)
names_gen = {n: 0.001 for n in names}
print(img_base)


font = './bb3810/hard.otf'

wc = WordCloud(font_path=font, background_color="white", max_words=2000, mask=img_base)
# wc.generate_from_frequencies(names_gen)
wc.generate(name_co)

plt.figure()
plt.imshow(wc)
plt.show()
