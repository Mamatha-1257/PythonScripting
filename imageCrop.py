from PIL import Image
  
# Opens a image in RGB mode
im = Image.open("/home/mamatha/Desktop/SampleData/White Bishop_00000.png")
im.show() 
# Setting the points for cropped image
left = 360 
top = 10
right = 600
bottom = 470
newPath = "./cropData/"
print(im) 
im1 = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
im1.show()
im2 = im1.crop((left, top, right, bottom))
im2.show()
rename =  "y" + ".png"
im2.save(newPath+rename)
