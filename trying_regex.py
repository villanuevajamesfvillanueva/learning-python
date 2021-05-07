import re

w = "My 2 favorite numbers are 19 and 42"
x = re.findall("[0-9]+", w)
y = re.findall("[AEIOU]+", w)
z = re.findall("[aeiou]+", w)
print(x)
print(y)
print(z)
print("\n\n")
w = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008\nstephen.marquard@gmail.com Sat Jan 5 10:14:16 2008"
a = re.findall("\S+@\S+", w)
print(a)
b = re.findall("\S@\S", w)
print(b)
c = re.findall("^From (\S+@\S+)", w)
print(c)
d = re.findall("[a-z0-9]+", w)
print(d)
e = re.findall('\S+?@\S+', w)
print(e)
e = re.findall('@\S+', w)
print(e)


numbers = [2.5, 3, 4, -5]

# start parameter is not provided
print(sum(numbers))
