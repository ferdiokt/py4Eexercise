# Import library needed
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Enter url
url = input('Enter url:')

# Ignore SSL error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Parsing url and find the tags
data = urllib.request.urlopen(url, context=ctx).read()
input = ET.fromstring(data.decode())
counts = input.findall('comments/comment')
print('Count:', len(counts))

# Listing the number
numlst = list()
for item in counts:
    num = item.find('count').text
    count = int(num)
    numlst.append(count)

print('Sum of all the number is:', sum(numlst))
