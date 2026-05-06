  # Positional Arguments
#  the arguments that need to be passed in the correct position
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")



print(greet("Almoiz", 23))  # Output: Hello, my name is Almoiz and I am 23 years old.




# Default Arguments
# the arguments that assume a default value if a value is not provided in the function call
def greet(name, age=23):
    print(f"Hello, my name is {name} and I am {age} years old.")

print(greet("Almoiz", 23))  # Output: Hello, my name is Almoiz and I am 23 years old.
print(greet("Almoiz"))       # Output: Hello, my name is Almoiz and I am 0 years old.




# Keyword Arguments
# the arguments that are passed to the function by explicitly stating the name of the parameter and its value
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

print(greet( age=24, name="Almoiz"))  # Output: Hello, my name is Almoiz and I am 23 years old.