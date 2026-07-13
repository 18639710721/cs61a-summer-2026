
# Functions as inputs  

# abstract common pattorn
"""
def sum_of_squares(n):
    i = 1
    total = 0
    while i <= n:
        total += i ** 2
        i += 1
    return total

def sum_of_cubes(n):
    i = i 
    total = 0
    while i <= n:
        total += i ** 3
        i += 1
    return total
"""

def squares(n):
    return n ** 2

def cubes(n):
    return n ** 3




def summation(n, term):
    i = 1
    total = 0
    while i <= n:
        total += term(i)
        i += 1
    return total



print(summation(5, squares))
