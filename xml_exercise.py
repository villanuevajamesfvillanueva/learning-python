from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1035245.xml"
xml = urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)
lst = tree.findall(".//comment")
print("Count: ", len(lst))
total = 0
for item in lst:
    num = int(item.find("count").text)
    total += num
print("Sum: ", total)
