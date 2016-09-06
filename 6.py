import os
import urllib
import zipfile
import re

##########################################################################
### These operations are required to download and extract the zip file  ###
##########################################################################
dir_riddle_6 = '6'
if not os.path.exists(dir_riddle_6):
  os.makedirs(dir_riddle_6)
os.chdir(dir_riddle_6)

file_zip = '6.zip'
if not os.path.exists(file_zip):
  urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip', file_zip)

zip_ref = zipfile.ZipFile(file_zip, 'r')
zip_ref.extractall('.')
zip_ref.close()

#########################################################################
###                  Here it starts the riddle                        ###
#########################################################################

readme = "readme.txt"
f = open(readme, 'r')

comments = []
while True:
  content = f.read()
  print content
  try:
    nothing = re.search(r"(\d{2,})", content).group()
  except:
    break
  f = open("%s.txt" % nothing, 'r')
  comments.append(zip_ref.getinfo("%s.txt" % nothing).comment)

print ''.join(comments)

#########################################################################
###            Extracts letters from the partial solution             ###
#########################################################################

import string 

link = ""
for line in comments:
  for p in line:
    if p in string.ascii_uppercase:
      if p not in link:
         link = link + p

print "The link is: " + link.lower() +".html\n"
