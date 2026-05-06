# Global variables are variables that are defined outside of a function and can be accessed and modified inside the function using the global keyword. below is its implementation
def sum(a, b):
    print("Hey I am summing ")
    c = a + b
    global z # Please modify global z
    z = 0 # This will refer to global z and not create a local variable
    return c 

z = 3
print(sum(3, 12))
print(z)