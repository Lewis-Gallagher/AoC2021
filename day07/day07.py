import numpy as np

def calc_fuel_costs(pos, fuel_costs = []):

    for i in range(min(pos), max(pos) + 1):
        fuel_costs.append(sum([abs((j - i)) for j in pos]))

    val, idx = min((val, idx) for (idx, val) in enumerate(fuel_costs))

    return val, idx


def calc_fuel_costs2(pos):

    fuel_costs = []

    for i in np.arange(min(pos), max(pos) + 1):
        li = []
        for j in pos:
            dist = abs(j - i)
            dist_sum = sum(np.arange(0, dist + 1))
            li.append(dist_sum)
        fuel_costs.append(np.sum(li))

    val, idx = min((val, idx) for (idx, val) in enumerate(fuel_costs))

    return val, idx

# Input
with open("day07/input.txt", "r") as infile:
    positions = [int(i) for i in infile.read().split(",")]

p1val, p1idx = calc_fuel_costs(positions)
p2val, p2idx = calc_fuel_costs2(positions)
print(p1val, p2val)