import urllib
import zipfile
import re

##########################################################################
###   These operations are required to download and open the zip file  ###
##########################################################################
file_zip = '6.zip'
urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip', file_zip)
zip_ref = zipfile.ZipFile(file_zip, 'r')

#########################################################################
###                  Here it starts the riddle                        ###
#########################################################################
fname = "readme.txt"

comments = []
while True:
  content = zip_ref.read(fname)
  print content
  try:
    nothing = re.search(r"(\d{2,})", content).group()
    fname = "%s.txt" % nothing
  except:
    break
  comments.append(zip_ref.getinfo(fname).comment)

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
