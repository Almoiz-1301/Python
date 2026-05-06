# Write a program that keeps asking the user to enter a password until they enter the correct one

correct_passsword = "secure123"

password = input("Enter the password: ")

while password != correct_passsword:
    print("Incorrect password. Please try again.")
    password = input("Enter the password: ")
print("Access granted. Welcome!")