# Calculate sum of numbers in a list recursively

def linear_sum(a:list)->int:
    i = 0
    size = len(a)-1
    if(i == size):
        return a[i]
    else:
        return  a[i]+ linear_sum(a[i+1:])


b = [1,2,3,4]
print(linear_sum(b))