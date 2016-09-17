from PIL import Image
import requests, cStringIO

#download the image
image_file = 'evil2.gfx'
r = requests.get('http://www.pythonchallenge.com/pc/return/' + image_file, auth=requests.auth.HTTPBasicAuth('huge', 'file'))

for i in range(5):
  image_raw = r.content[i::5]
  im = Image.open(cStringIO.StringIO(image_raw))
  f = open("%d.%s" % (i, im.format.lower()), "wb")
  f.write(image_raw)
  f.close()