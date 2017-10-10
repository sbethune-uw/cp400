
# CP400 - Single Dice Simulation
from random import randint

l = []
for x in range(0, 1000000):
    rc = 1
    a = 0

    while rc <= 3:
        a = int(randint(1, 6))
        if a > 4:
            l.append(a)
            break
        else:
            rc += 1

    if rc == 4:
        l.append(a)

print sum(l) / float(len(l))
#print l[:]
