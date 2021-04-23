import os
from PIL import Image

SRC = "/home/mamatha/Desktop/SampleData/"
DES = "/home/mamatha/Desktop/final/"

LEFT = 360
TOP = 10
RIGHT = 600
BOTTOM = 470

for img in os.listdir(SRC):
    
    im = Image.open(SRC + img)
    im.show()

    resizedImg = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)),Image.ANTIALIAS)
    resizedImg.show()

    croppedImg = resizedImg.crop((LEFT, TOP, RIGHT, BOTTOM))
    croppedImg.show()

    finalImg = croppedImg.resize((160, 300), Image.ANTIALIAS)
    finalImg.show()

    rename =  img.split('.')[0] + "z" + ".png"
    
    finalImg.save(DES + rename, optimize=True, quality=95)
