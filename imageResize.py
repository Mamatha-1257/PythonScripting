from PIL import Image
import os
path = "./SampleData/"
newPath = "./newpath/"
for img in os.listdir(path):
    print(str(img))
    im = Image.open(path + img)
    im.show()
    resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
    resized_im.show()
    rename =  img.split('.')[0] + "x" + ".png"
    resized_im.save(newPath+rename)

