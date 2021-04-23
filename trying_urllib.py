import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = {}
for line in fhand:
    text = line.decode().strip()
    print(text)
    print(type(text))
    words = line.decode().split()
    #print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        #print(counts)
print(counts)