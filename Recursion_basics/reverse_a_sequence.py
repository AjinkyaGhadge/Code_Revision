#Program to reverse an array recursively. 


def reverse_recursive(l:list,front,rear)->list:
    if front>rear:
        return l
    else:
        l[front],l[rear] = l[rear],l[front]
        print(l)
        return reverse_recursive(l,front+1,rear-1)

d = [1,2,3,4,5]
print(reverse_recursive(d,0,4))
