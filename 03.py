import urllib
import re

page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').readlines()[21:]
print "The url is " + "".join(re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", "".join(page))) + ".html"

