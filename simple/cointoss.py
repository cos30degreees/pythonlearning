from random import randint

numHeads = 0
numTails = 0

for t in range(100):
    if randint(1, 2) == 1:
        numHeads += 1
    else:
        numTails += 1
        
print('There were %s heads and %s tails' % (numHeads, numTails))
