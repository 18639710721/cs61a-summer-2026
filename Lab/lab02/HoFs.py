def square(x):
    return x * x

def scale(f, x, k):
    """Returns the result of f(x) scaled by k."""
    return k * f(x)

# Functions that return functions

def multiply_by(m):
    def multiply(n):
        return n * m
    return multiply


