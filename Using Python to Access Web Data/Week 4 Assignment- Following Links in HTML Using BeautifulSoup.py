# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
'''
url = input('Enter - ')
count = int(input("Enter count: "))
pos = int(input("Enter position:"))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
url2 = tags[pos-1].get('href',None)


for i in range(count-1):
    html = urllib.request.urlopen(url2, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url2 = tags[pos-1].get('href',None)
#    print(url2)
print(re.findall("known_by_(.+)\.",url2)[0])
'''
url = None
while True:
    if url == None:
        url = input('Enter - ')
        count = int(input("Enter count: "))
        pos = int(input("Enter position:"))
    else:
        for i in range(count):
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            url = tags[pos-1].get('href', None)
        break

print(re.findall("known_by_(.+)\.", url)[0])
