#Program to calculate a number raised to a specific power recursively

def power_rec(n:int, p:int):
    if p == 1:
        return n
    else:
        return n * power_rec(n,p-1)

print(power_rec(5,3))