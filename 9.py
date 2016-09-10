from PIL import Image
import requests
import re
from StringIO import StringIO


#downland the pixel coordinates from the page source that should be connected
page = 'good.html'
r = requests.get('http://www.pythonchallenge.com/pc/return/' + page, auth=requests.auth.HTTPBasicAuth('huge', 'file'))
first = re.search(r'first:((.|\n)*)second', r.content).group(1) 
second = re.search(r'second:((.|\n)*)-->', r.content).group(1) 
first = first.split(',')
second = second.split(',')

#connect all the dots together 
all_dots = first + second

#create a new image in which connect the pixel
new_image = Image.new('RGB', (640,480))
pix = new_image.load()
for i in range(0, len(all_dots), 2):
  x = int(all_dots[i])
  y = int(all_dots[i+1])
  #insert a white pixel
  pix[x, y] = (255, 255, 255, 255)

new_image.show()

print "\nThe url is bull.html"