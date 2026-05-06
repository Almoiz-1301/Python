# Use a while loop to reverse a given number (e.g., 123 → 321).
# num = 453322
# print(int(str(num)[::-1]))

num = int(input("Enter a number to reverse: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed number:", reversed_num)