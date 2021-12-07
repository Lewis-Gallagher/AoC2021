import numpy as np

with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

    # Get data into list of lists of [[x1,y1], [x2,y2]] e.g. [[427, 523], [427, 790]] etc.
    strings = [line.split(" -> ") for line in lines]
    string_pairs = [[j.split(",") for j in i] for i in strings]
    int_pairs = [[[int(k) for k in j] for j in i] for i in string_pairs]

empty_matrix = np.zeros(max([[max(i) + 1 for i in j] for j in int_pairs]))

for coords in int_pairs:
    
    # Is the line vertical? (x1 == x2)
    if (coords[0][0] == coords[1][0]):
        
        # x1 is the smallest and x2 the biggest of the pair
        x1 = min([coords[0][1], coords[1][1]])
        x2 = max([coords[0][1], coords[1][1]])
        
        # y is the same so can be either
        y = coords[0][0]
        
        # Update the grid
        empty_matrix[x1:x2+1, y] += 1
    
    # Is the line horizontal (y1 == y2)
    elif (coords[0][1] == coords[1][1]):
        
        # y1 is the smallest and y2 the biggest of the pair
        y1 = min([coords[0][0], coords[1][0]])
        y2 = max([coords[0][0], coords[1][0]])
        
        # x is the same so can be either
        x = coords[0][1]

        # Update the grid
        empty_matrix[x, y1:y2+1] += 1

print((empty_matrix > 1).sum())