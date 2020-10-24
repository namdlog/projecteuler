l = []
z = 0
for a in range(334):
    if (3*a%5) != 0:
        l += [3*a]
        z += 3*a
    if(5*a<1000):
        l += [5*a]
        z += 5*a

print(l)
print(z)