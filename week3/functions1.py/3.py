def solve(numheads, numlegs):
    chickens=numheads
    rabbits=0
    while chickens*2+rabbits*4!=numlegs:
        chickens-=1
        rabbits+=1
    return chickens, rabbits
print(solve(35,94))