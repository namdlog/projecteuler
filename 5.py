def mmc(a,b):
    for c in range(1,1000):
        if((c*a)%b == 0):
            k = c*a
            break
    return k

print(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(mmc(1,2),3),4),5),6),7),8),9),10),11),12),13),14),15),16),17),18),19),20))