import re
#one liner flex
print(sum([int(i) for i in re.findall("[0-9]+", open("regex_sum_1035241.txt", "r").read())]))

textfile = "regex_sum_1035241.txt"
with open(textfile, "r") as f:
    contents = f.read()
    nums = re.findall("[0-9]+", contents)
    total = 0
    for num in nums:
        total += int(num)
    print(total)
