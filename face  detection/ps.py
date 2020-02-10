from PIL import Image


im = Image.open('rohit.jpg')
fp = open("rohit.jpg", "rb")
im = Image.open(fp)
im.show()
print('Image Format: ', im.format)
print("Size of Image WxH: %dx%d" % im.size)
print('Color Model: ', im.mode)


        
    
    
    #print(imagespath)
#show the images file    
#GetImagesWithId(path)
    
