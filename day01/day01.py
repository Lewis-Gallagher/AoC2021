import more_itertools

with open("day01/input.txt", "r") as depth:

    up = 0
        
    depth = [int(i) for i in depth.read().splitlines()]
    
    for i, j in more_itertools.pairwise(depth):
        if i < j:
            up += 1

    print(f"Part 1: {up} increases")

    win_size = 3
    
    up = 0
    win_sums = []
    
    for e,i in enumerate(range(len(depth) - win_size + 1), start = 1):
        
        win_sum = sum(depth[i: i + win_size])
#         win_sums = [int(i) for i in win_sums]

#         print(e, win_sum)
        
        win_sums.append(win_sum)
        
    for i, j in more_itertools.pairwise(win_sums):
        if i < j:
            up += 1

    print(f"Part 2: {up} increases")