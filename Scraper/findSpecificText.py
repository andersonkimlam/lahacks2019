import urllib2
from BeautifulSoup import BeautifulSoup
import re

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0' )]

url = ('http://en.wikipedia.org/wiki/Bayside_(band)')

ourUrl = opener.open(url).read()

soup = BeautifulSoup(ourUrl)

title = soup.title.text

body = soup.find(text = "Origin").findNext('td')
outfile = open('/projects/training/wikipedia.txt', 'w')
outfile.write(body.text)
