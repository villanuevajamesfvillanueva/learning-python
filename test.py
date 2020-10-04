#BOUNCER

age = input("Enter your age: ")
int_age = int(age)

if int_age < 18:
    print("Go home nigga, you too young")

elif int_age >= 18 and int_age < 32:
    print("Yo homie, let's goooo")

elif int_age >= 32 and int_age <= 60:
    print ("Yo come in")


else:
    print("Damn bro you old, but you can come in")

print("End.")