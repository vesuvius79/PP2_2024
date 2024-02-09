def solve(numheads, numlegs):
    return "rabbits:", numlegs / 2 - numheads, "chickens:", numheads * 2 - numlegs / 2

print(solve(35, 94))