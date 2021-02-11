# Import library needed
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Input
url = input('Enter url:')
count = int(input('Enter count:'))
pos = int(input('Enter position:'))


# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Html parser and beautifulsoup access
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Creating tags
tags = soup('a')
namelist = list()
while count >= 1:
    # Retrieving tag based on position
    clicklink = tags[pos - 1]
    url = clicklink.get('href', 2)

    # Retrieving name from the url
    name = re.findall('http://py4e-data.dr-chuck.net/known_by_(\S+).html', url)
    namelist.append(name)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieving tags from the new url clicked
    tags = soup('a')
    count -= 1

# Get the last name from the last link clicked
lastname = namelist[-1]
print('Last name found:', lastname)
