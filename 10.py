import math

def isPrime(n):
    if n%2 == 0:
        return False
    for a in range(3,int(math.sqrt(n))+1,2):
        if n%a == 0:
            return False
    return True

b = 2

for a in range(3,2000000,2):
    if isPrime(a):
        b += a

print(b)