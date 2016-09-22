import re
import urllib

nothing = "12345"
while True:
   page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing).read()
   print page
   try:
      nothing = re.search(r"(\d+)", page).group()
   except:
      break