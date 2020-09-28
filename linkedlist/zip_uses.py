# How useful can zip be?


l1 = [1,2,3,4,5,6,7,8]
l2 = [8,7,6,5,4,3,2,1]

for x,y in zip(l1,l2):
    print(x,y)
print(type(y))