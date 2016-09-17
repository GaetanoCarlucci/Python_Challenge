import requests
import xmlrpclib

server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print "List of remote methods:"
print server.system.listMethods()

#Who is the evil? 
print "\nWho is the evil?"
#The answer is here!
image_file = 'evil4.jpg'
r = requests.get('http://www.pythonchallenge.com/pc/return/' + image_file, auth=requests.auth.HTTPBasicAuth('huge', 'file'))
print r.content

"Bert phone number is:"
print server.phone('Bert')

print "The next url is italy.html"