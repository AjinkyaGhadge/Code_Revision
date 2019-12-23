# Recursive Python function that finds the minimum and maximum values in a sequence

def recursive_sort(l:list,front,rear):
    if front<rear:
        for i in range(front,rear):
            if l[i]<l[front-1]:
                l[i],l[front-1] = l[front-1],l[i]
        front+=1
        return recursive_sort(l,front,rear)
    else:
        return l

def max_list(l):
    recursive_sort(l,1,len(l))
    return(l[0])

def min_list(l):
    recursive_sort(l,1,len(l))
    return(l[len(l)-1])

a = [5,4,3,2,1]
print(recursive_sort(a,1,5))
print(max_list(a))
print(min_list(a))