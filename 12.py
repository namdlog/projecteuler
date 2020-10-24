l = [0]

def divisores(n):
    cont = 0
    for a in range(1,n):
        if((n%a) == 0):
            cont += 1
    return cont

for a in range(10001):
    l += [l[len(l)-1]+a]

print(divisores(l[len(l)-11]))
