# Import library needed
import urllib
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Url access and beautifulsoup usage
url = input('Enter url:')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieving tag
numlist = list()
tags = soup('span')
for tag in tags:
    num = int(tag.contents[0])
    numlist.append(num)

print('Sum of the number in page:', sum(numlist))
