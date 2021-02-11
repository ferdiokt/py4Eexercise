# Import the library needed
import urllib.request
import urllib.parse
import urllib.error
import ssl
import json

# Enter url
url = input('Enter url:')

# Ignore SSL error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Parsing html data from url
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data.decode())
print('Counts:', len(info['comments']))

# Accessing number from the count tag
numlst = list()
for item in info['comments']:
    num = int(item['count'])
    numlst.append(num)

print('Sum of the number is:', sum(numlst))
