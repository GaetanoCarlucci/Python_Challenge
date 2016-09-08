from PIL import Image
import urllib
import re

#download the image
image_file = 'oxygen.png'
urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/' + image_file, image_file)

#open the image
im = Image.open(image_file, 'r')
#load the image
pix = im.load()
#Get the width and hight of the image for iterating over
(width, hight) = im.size 
print "Image size: " + str((width, hight))
#print pix[x,y] #Get the RGBA Value of the a pixel of an image
#pix[x,y] = (0,0,0,0) # Set the RGBA Value of the image (tuple)
#im.save("output.png") # Save the modified image

#Prints all the corresponding ascii of the pixel that have been modified in the image. There are 7 consecutive pixel with the same value.
output1 = ''.join([chr(pix[i,hight/2][0]) for i in range(0, width, 7)])
print output1

#Prints all the corresponding ascii of string extracted from the image
output2 = re.search(r'\[(.*?)\]', output1).group(1)
print "\nThe url is " + ''.join([chr(int(i)) for i in output2.split(',')]) + ".html"