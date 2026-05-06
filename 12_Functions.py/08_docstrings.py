# Docstrings are used to document functions, classes, and modules. In Python, they are written in triple quotes. They are accessible using the __doc__ attribute. Here's an example:
# Docstring for a function is the first statement in the function body. It is used to describe what the function does. It can also be used to describe the parameters and the return value of the function. Below is its implementation:
def sum(a, b): 
    '''This will sum two numbers'''
    c = a + b  
    return c

print(sum.__doc__)


def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b

print(add.__doc__)