#!/usr/bin/env python
# created by yao
# inproved by superping
# 2016.12.23
import sys, getopt
from PIL import Image


def main(argv):
	inputfile = ''
	start = 12
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:s:",["ifile=","startY="])
	except getopt.GetoptError:
		print 'getMoney.py -i <inputfile> -s <startY>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'getMoney.py -i <inputfile> -s <startY>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-s", "--start"):
			start = arg
	print 'inputfile:', inputfile
	print 'startY:', start


	im = Image.open(inputfile)

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


	im.save(inputfile+'.dealed.jpg')
	im.show()

if __name__ == "__main__":
   main(sys.argv[1:])

