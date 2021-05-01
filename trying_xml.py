import xml.etree.ElementTree as ET

data = """<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>"""

tree = ET.fromstring(data)
print(type(tree))
print("Name: ", tree.find("name").text)
print("Phone number: ", tree.find("phone").text.strip())
print("Arrt: ", tree.find("email").get("hide"))
print(type(tree.find("name").text))


data2 = """<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>"""

stuff = ET.fromstring(data2)
lst = stuff.findall("users/user")
print("\n\n")
print(lst)
print("User count: ", len(lst))
for item in lst:
    print("Name", item.find("name").text)
    print("Id", item.find("id").text)
    print("Attribute: ", item.get("x"))