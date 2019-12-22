def ispallindrome(palstring:str):
    l = list(palstring)
    fp = 0
    rp = len(l)-1
    while(fp<=rp):
        if(l[fp] == l[rp]):
            fp=fp+1
            rp=rp-1
        else:
            return False
    return True



s = [1,2,3,4,5,6,7,8]
k = enumerate(s)
for i in k:
    print (i)

d = {'a':1,'b':2,'c':3}
for i,j in enumerate(d):
    print(i,j)