import urllib
import bz2
import re

def decode(line):
   out = re.search(r"\'(.*?)\'",''.join(line)).group()
   out = eval("b%s" % out)
   return bz2.decompress(out)

#read lines that contain the encoded message
page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').readlines()[20:22]

print "Click on the bee and insert: "
User_Name = decode(page[0])
print "User Name is: " + User_Name
Password = decode(page[1])
print "Password is: " + Password