inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

data = []
for item in inventory:
    entries = item.split()
    for i in entries:
        data.append(i)

index = -1
for entry in data:
    index += 1
    if entry[-1] == ",":
        entry = entry[:-1]
        data[index] = entry

max = len(data)
for x in range(0,max,3):
    print(f"The store has {data[x+1]} {data[x]}, each for {data[x+2]} USD")
    