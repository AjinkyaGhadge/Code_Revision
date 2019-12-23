# Recursive Python function that finds the minimum and maximum values in a sequence

def min_list(l,front,rear):
    if(front<rear):
        if(l[front]<l[0]):
            l[front],l[0] = l[0],l[front]
        return min_list(l,front+1,rear)
    else:
        return l[0]

def max_list(l,front,rear):
    if(front<rear):
        if(l[front]>l[0]):
            l[front],l[0] = l[0],l[front]
        return max_list(l,front+1,rear)
    else:
        return l[0]

a = [4,2,56,1,-100,-50]
print(max_list(a,1,len(a)))