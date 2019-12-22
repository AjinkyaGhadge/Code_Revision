def binary_search(l:list,n:int)->int:
    mid = len(l)//2
    if l[mid] == n:
        return mid
    elif l[mid]<n:
        return binary_search(l[mid:],n)
    elif l[mid]>n:
        return binary_search(l[0:mid],n)
    else:
        return -1