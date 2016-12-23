#!/usr/bin/env python
# created by yao
# improved by superping
# 2016.12.23
import sys
from PIL import Image
im = Image.open(sys.argv[1])

xsize, ysize = im.size
#imgWidth = 370 # width of the image you cut off
startY = 18 # the first line position-y
splitPoxis = 18 # split height
blackHeigh = 8 # black line height
maxLineNumber = 27


# function to deal image
def pasteImg( startY, index):
    box = (1, startY + splitPoxis*index-blackHeigh,xsize,startY + splitPoxis*index)
    region = im.crop(box)
    
    box_dealed = (1,startY + splitPoxis * index,xsize,startY + splitPoxis*index+blackHeigh)
    region_dealed = im.crop(box_dealed)
    
    im.paste( region, box_dealed )


pasteImg(startY, 0)

for index in range(1,maxLineNumber):
    pasteImg( startY, index )


im.save(sys.argv[1]+'.dealed.jpg')
im.show()
