import os
from PIL import Image

path = "./SampleData/"
newPath = "./cropData/"
intPath = "./resizeData/"
left = 360
top = 10
right = 600
bottom = 470

for img in os.listdir(path):
    
    im = Image.open(path + img)
    im.show()

    resizeImg = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
    rename =  intPath + img.split('.')[0] + "x" + ".png"
    resizeImg.save(rename, optimize=True,quality=95)
    resizeImg.show()

    cropImg = resizeImg.crop((left, top, right, bottom))
    rename =  img.split('.')[0] + "y" + ".png"
    cropImg.save(newPath+rename, optimize=True,quality=75)
    cropImg.show()


