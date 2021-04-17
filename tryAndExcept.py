largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
        
    try:
        num = int(num)
        if largest is None or num > largest:
            largest = num
        elif smallest is None or num < smallest:
            smallest = num
            
    except:
        print("Invalid input")
        continue
            
print("Maximum is", largest)
print("Minimum is", smallest)