# Print the multiplication table of a number (entered by user).
num = int(input("Enter the number for the table to be printed:"))
for i in range(1,11):
    print(num ,"X",i,"=",num*i)
