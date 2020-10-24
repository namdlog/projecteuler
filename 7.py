import math

l = [2,3,5,7]

def isPrime(n):
    k = 1
    for a in range(2,math.ceil(math.sqrt(n)+1)):
        if((n%a) == 0):
            k = 0
            break
    if(k == 1):
        return 1
    else:
        return 0

for b in range(8,110000):
    if(isPrime(b)):
        l += [b]

print(l[10000])