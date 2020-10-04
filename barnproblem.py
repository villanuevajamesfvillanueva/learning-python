#Solving number of Pigs, Chickens, and Spiders
print("---This program solves the number of chickens, pigs, and spiders given total heads and total legs---")

def solve(numLegs, numHeads):
    soln = []
    for numSpidies in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpidies + 1):
            numPigs = numHeads - numChicks - numSpidies
            ansLegs = 4*numPigs + 2*numChicks + 8*numSpidies
            if (ansLegs == numLegs):
                soln.append(numPigs)
                soln.append(numChicks)
                soln.append(numSpidies)
    return soln

numHeads = int(input("Enter number of heads: "))
numLegs = int(input("Enter number of legs: "))
soln = solve(numLegs, numHeads)

if not soln:
    print("There are no solutions.")
else: 
    print("\nSolutions are: ")
    sets = int(len(soln)/3)
    for i in range(0, sets):
        print(f"{soln[0 + 3*i]} pigs, {soln[1 + 3*i]} chickens, and {soln[2 + 3*i]} spiders")
