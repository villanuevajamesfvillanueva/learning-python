from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1035243.html"
url2 = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urlopen(url2, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
tags = soup('a')
for tag in tags:
    #total += int(tag.contents[0])
    print(tag.get('href', None))
    print(type(tag.get('href', None)))
print(total)
    
