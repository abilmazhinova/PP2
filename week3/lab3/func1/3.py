numheads=int(input())
numlegs=int(input())

def solve(numheads, numlegs):
    rabbits = 0.5 * numlegs - numheads
    chickens = 2 * numheads - 0.5 * numlegs
    return (rabbits, chickens)
print(solve(numheads, numlegs))


