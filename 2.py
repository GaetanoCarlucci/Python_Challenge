import urllib
import re

page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').readlines()[38:]
print "The link is " + "".join(re.findall(r"[a-z]+", ''.join(page))) + ".html"