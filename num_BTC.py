import math

def num_BTC(b):
    if b < 1:
        return 0
    reward = 50
    total = 50
    count = 1
    for block in range(1,b):
        total += reward
        count += 1
        if count == 210000:
            reward = reward/2
            count = 1
    
    return float(total)


