import pickle
import urllib

text = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
data = pickle.loads(text)

for row in data:
  print ''.join([p[0] * p[1] for p in row])