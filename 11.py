from PIL import Image
import requests, cStringIO
import re


#download the image
image_file = 'cave.jpg'
r = requests.get('http://www.pythonchallenge.com/pc/return/' + image_file, auth=requests.auth.HTTPBasicAuth('huge', 'file'))

#open the image
im = Image.open(cStringIO.StringIO(r.content))
#load the image
pix = im.load()
#Get the width and hight of the image for iterating over
(width, hight) = im.size 

#create a new images in which store odd and even pixels
new_image_odd = Image.new('RGB', (width,hight))
new_image_even = Image.new('RGB', (width,hight))
pix_odd = new_image_odd.load()
pix_even = new_image_even.load()

for i in range(width):
   for j in range(hight):
      if (j+i) % 2 == 0:   
         pix_even[i,j] = pix[i,j]
      else:
         pix_odd[i,j] = pix[i,j]

new_image_odd.show()
new_image_even.show()