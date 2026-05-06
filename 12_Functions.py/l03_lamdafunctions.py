# lamda functions are anonymous functions that can be defined in a single line. They are often used for short, simple operations.
# The syntax for a lambda function is: lambda arguments: expression
square = lambda x: x*x 
'''
As good as writing
def square(x):
    return x*x
'''
sum = lambda x, y: x+y
'''
As good as writing
def sum(x, y):
    return x + y
'''

print(square(3))
print(sum(3, 62))