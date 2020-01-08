# Program to check if a string is a palindrome using hashing

def hash (hs:str):
    hval = 0
    j = 1
    for i in hs:
        hval = hval+(ord(i)*j)
        j+=1
    return hval

