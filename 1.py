import string 

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

intab =  string.ascii_lowercase
outtab = intab[2:] + intab[:2]
trantab = string.maketrans(intab, outtab)

print message.translate(trantab)

link = "map"

print "\nThe link is: " + link.translate(trantab) + ".html"