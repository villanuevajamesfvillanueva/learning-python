import random

rand_num  = random.randint(1,6)

print("\nNUMBER GUESSING GAME")
lives = 5
tries = 1

def guess():
    guess = int(input("\nInput guess: "))
    return guess

print(rand_num) #to see the correct answer

x = guess()
if x == rand_num:
    print("Good job! YOU WIN.\n")
    print("It only took you 1 try.")

else:
    while (x != rand_num) and (lives > 0):
        tries += 1
        lives -= 1
        print("Incorrect. Please try again")
        print("lives left: " + str(lives))
        x = guess()

        if x == rand_num:
            print("Good job! YOU WIN.")
            print("It took you " + str(tries) + " tries.\n")
        
if lives == 0:
    print("YOU LOSE.\n")   


#indicate mechanics: range of numbers that player will guess
#put levels
#check for input (must be int only)