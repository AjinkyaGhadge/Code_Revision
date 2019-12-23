# Recursive program to compute the product of two positive integers,
# m and n, using only addition and subtraction.

def product(m:int,n:int)->int:
    if n>1:
        return m+product(m,n-1)
    else:
        return m

print(product(2,3))