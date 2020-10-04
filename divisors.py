import time
start_time =  time.time()

print("\nGETTING THE DIVISORS OF A NUMBER")
given = int(input("Give me a number: "))
divisor = 1
pair = given
soln = [ ]

if given >= 0:
    while divisor <= pair:
        r = given%divisor
        if r == 0 and divisor not in soln:
            pair = given/divisor
            soln.append(divisor) 
            soln.append(int(pair))              #appending current divisor and quotient, moving towards center
            if pair == divisor:                 #avoiding duplicates
                soln.pop()                          
        divisor += 1
    
    soln.sort()
    print(soln)
    count = len(soln)
    print("There are " + str(count) + " divisors of " + str(given) + ".")

else: print("The number is negative!")
execTime = round(time.time() - start_time, 2)
print("\nProgram executed in " + str(execTime) + " sec")



