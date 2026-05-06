# create a Program that checks the age of the person and then tells them whether they are eligible for voting or not. (voting age >= 18 years)

age = int(input("Enter your age to check voting eligiblity:  "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")