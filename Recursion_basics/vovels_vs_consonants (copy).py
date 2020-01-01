# Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.

def ismorevowels(l:list,v:int,c:int,s:int,vovl,i):
    if s == i:
        if v>c:
            return True
        else:
            return False
    if i<s:
        if l[i] in vovl:
            return ismorevowels(l,v+1,c,s,vovl,i+1)
        else:
            return ismorevowels(l,v,c+1,s,vovl,i+1)
 
vovl = ['a','e','i','o','u']
l = ['a','e','i','j','k','f','e','h','o']
print(ismorevowels(l,0,0,9,vovl,0))