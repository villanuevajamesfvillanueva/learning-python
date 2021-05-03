import json
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving ", url)
handle = urllib.request.urlopen(url, context = ctx).read()
print("Retrieved ", len(handle), "characters")
data = handle.decode()
js = json.loads(data)
total = 0
count = 0
for i in js["comments"]:
    total += int(i["count"])
    count += 1
print("Count: ", count)
print("Sum: ", total)