import urllib
import urllib.request
import re

#connect to a URL
website = urllib.request.urlopen("http://thepage.surge.sh/",data=None)

#read html code
html = website.read()

html = html.decode('ASCII')

#use re.findall to get all the links
links = re.findall('"((http|ftp)s?://.*?)"', html)
print(html)
print(links)