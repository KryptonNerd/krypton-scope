# Stacking.py
from PIL import Image
import glob
import numpy as np

def stack_images(folder,filetype):

    imgList = glob.glob(folder + filetype)


    first = True
    i=0

    for img in imgList:
        print(i)
        i+=1
        imgRGB = np.asarray(Image.open(img))
        imgRGB = imgRGB.astype('uint32')
        if first:
            sumImage = imgRGB

            first = False
        else:
            sumImage = sumImage + imgRGB


    avgArray = sumImage/len(imgList)
    avgImg = Image.fromarray(avgArray.astype('uint8'))
    avgImg.show()
    avgImg.save('stackedPicture.tiff',format='TIFF')


#stack_images('Test_Images\M31_TIFF','\*.tiff')