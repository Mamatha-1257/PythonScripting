import os
from PIL import Image

SRC = "/home/mamatha/Desktop/SampleData/White_Knight_Color_0_1/Use/"
DES = "/home/mamatha/Desktop/final/"

sizes = [250, 60, 700, 470]

for im in os.listdir(SRC):

    img = Image.open(SRC + im)

    resizedImg = img.resize((round(img.size[0]*0.5), round(img.size[1]*0.5)),Image.ANTIALIAS)

    croppedImg = resizedImg.crop((sizes[0], sizes[1], sizes[2], sizes[3]))
    croppedImg.thumbnail((224, 224))

    rename =  im.split('.')[0] + ".png"

    croppedImg.save(DES + rename, optimize=True, quality=95)





