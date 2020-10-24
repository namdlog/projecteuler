l = []
max = 1
r = 0
for a in range(1,1000000):
    k = a
    cont = 1
    while(k != 1):
        if(k%2 == 0):
            k /= 2
        else:
            k = (3*k)+1
        cont += 1
    if(cont > max):
        r = a
        max = cont

print(r)