# If their is multiple arguments to print then it adds space between them
print("Almoiz Age is" ,24, 'years old')


# The Print Function in Python 3 by default ends with a new line character due to which the next print statement prints in new line
print("Hello Almoiz!")
print("Welcome to Python programming.")
# To avoid this we can use end parameter of print function which by default is '\n' (new line character) and we can change it to anything we want
print("Hello Almoiz!", end=", ")
print("Welcome to Python programming.")

# We can also use sep parameter of print function to change the separator between multiple arguments of print function. By default it is a space character ' '
print("Almoiz", "is", "learning", "Python")
print("Almoiz", "is", "learning", "Python", sep="\t")  # tab space as separator
print("Almoiz", "is", "learning", "Python", sep="---")
