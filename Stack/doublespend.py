import math

pow1 = 0.4/0.6
exp4 = 0
for k in range(1,6):
    print(k)
    pow2 = 5-k
    exp1 =  math.pow(math.pow(5,pow1),k)
    exp2 = math.factorial(k) * math.pow(math.e,k)
    exp3 = math.pow((1-pow1),pow2)
    exp4 = exp4 + (exp1/exp2)*exp3
res = 1 - exp4

print(res)