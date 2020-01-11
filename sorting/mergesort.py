#Program to implement merge sort

def merge(arr,l:int,m:int,r:int):
    s1 = m-l+1
    s2 = r-m

    a1=list()
    a2=list()

    for i in range(0,s1):
        a1.append(arr[l+i])
    
    for i in range(0,s2):
        a2.append(arr[m+1+i])

    i,j,k = 0,0,l

    while i<s1 and j<s2:
        if a1[i] <= a2[j]:
            arr[k] = a1[i]
            i+=1
        else:
            arr[k] = a2[j]
            j+=1
        k+=1

    while i < s1:
        arr[k] = a1[i]
        i+=1
        k+=1

    while j<s2:
        arr[k]= a2[j]
        j+=1
        k+=1


def mergesort(arr,l,r):
    if l<r:
        m = int((l+(r-1))/2)
        mergesort(arr,l,m)
        mergesort(arr,m+1,r)
        merge(arr,l,m,r)


arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
mergesort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i])