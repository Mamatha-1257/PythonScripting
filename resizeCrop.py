import os
from PIL import Image

path = "/home/mamatha/Desktop/SampleData/"
newPath = "/home/mamatha/Desktop/cropData/"
intPath = "/home/mamatha/Desktop/resizeData/"
finalPath = "/home/mamatha/Desktop/final/"
left = 360
top = 10
right = 600
bottom = 470

for img in os.listdir(path):
    
    im = Image.open(path + img)
    im.show()

    resizeImg = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
    rename =  intPath + img.split('.')[0] + "x" + ".png"
    resizeImg.save(rename, optimize=True,quality=100)
    resizeImg.show()

    cropImg = resizeImg.crop((left, top, right, bottom))
    rename =  img.split('.')[0] + "y" + ".png"
    cropImg.save(newPath+rename, optimize=True,quality=100)
    cropImg.show()

    finalImg = cropImg.resize((160, 300), Image.ANTIALIAS)
    rename =  img.split('.')[0] + "z" + ".png"
    finalImg.save(finalPath + rename, optimize=True, quality=95)
    finalImg.show()
