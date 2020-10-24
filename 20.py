d = 1

for a in range(2,101):
    d *= a

k = str(d)
c = 0
for b in range(len(k)):
    c += int(k[b])

print(c)
