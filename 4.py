import re
import urllib

i = 0
nothing = "12345"
content = ""
while True:
   r = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing).read()
   print r
   try:
      nothing = re.search(r"(\d+)", r).group()
   except:
      break