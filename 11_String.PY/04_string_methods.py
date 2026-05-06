s = "hello world" # Strings are immutable

# s[0] = "R" # You cannot do this

a = len(s) # Length of string
# print(a)
# print(s.upper(), s) # Strings are immutable, original string will not change upper() returns a new string wihich is uppercase
# print(s.lower()) # returns a new string which is lowercase
# print(s.capitalize()) // First letter uppercase
# print(s.title()) // First letter of each word uppercase

# text = " \nhello world "
# print(text.strip()) # Output: "hello world"    // removes leading and trailing whitespace characters
# print(text.lstrip()) # Output: "hello world "  // removes leading whitespace characters from the left
# print(text.rstrip()) # Output: " hello world" // removes trailing whitespace characters from the right


# text = "Python is fun and fun and fun"
# print(text.find("is")) # Output: 7 Index of first occurence
# print(text.replace("fun", "awesome")) // Output: "Python is awesome and awesome and awesome"


# text = "Apples,Bananas,Pineapples"
# print(text.split(",")) // splits the string into a list of substrings based on the delimiter ","
# print(",".join(['Apples', 'Bananas', 'Pineapples']))  // joins the list of strings into a single string with "," as the separator

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False