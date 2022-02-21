import math

def num_BTC(b):
    if b < 1:
        return 0
    reward = 50.0
    total = 0
    count = 0
    #for block in range(0,b):
    #    total += reward
    #    count += 1
    #    if count == 210000:
    #        reward = reward/2
    #        count = 0
    

    rem = pow(b,1,210000)
    splits = b//210000
    for i in range(0,int(splits)):
        total += reward*210000
        reward = reward/2

    if rem > 0:
        total += rem*reward
    return float(total)

