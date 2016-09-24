from PIL import Image
import requests, cStringIO
import numpy as np

#download the image
image_file = 'wire.png'
r = requests.get('http://www.pythonchallenge.com/pc/return/' + image_file, auth=requests.auth.HTTPBasicAuth('huge', 'file'))
im = Image.open(cStringIO.StringIO(r.content))

#load the image
pix = im.load()
#Get the width and hight of the image for iterating over
(width, hight) = im.size 

#create a new images in which we store the rolled one
new_image = Image.new('RGB', (100,100))
(width_new, hight_new) = new_image.size 
pix_new = new_image.load()

x = 0
y = 0
border = 0
state = "right"

for h in range(width):
  pix_new[x,y] = pix[h,0]
  
  if state == "right":    
    if x < width_new - 1 - border:
      x = x + 1
    else:
      state = "down"
      y = y + 1
      continue

  if state == "down":
    if y <  hight_new - 1 - border:
       y = y + 1
    else:
      state = "left"
      x = x - 1
      continue

  if state == "left":
    if x > border:
      x = x - 1
    else:
      state = "up"
      y = y - 1
      border = border + 1
      continue

  if state == "up":
    if y > border:
      y = y - 1
    else:
      state = "right"
      x = x + 1
      continue

new_image.show()

print "The url is cat.html, the next level is uzi.html"