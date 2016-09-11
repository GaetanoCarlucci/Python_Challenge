def lookAndSay(a):
  out = ""
  count = 1
  for j in range(len(a)-1):
    if a[j] == a[j+1]:
      count = count + 1
    else:
      out = out + "%s%s" % (a[j], count)
      count = 1
  out = out + "%s%s" % (a[-1], count)
  return out

a = "1"
for i in range(30):
  a = lookAndSay(a)

print "The url is: " + str(len(a)) + ".html"