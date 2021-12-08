import numpy as np

def is_vertical(coordinates):

    """
    If x1 == x2 then the line is vertical (i.e. no change in x axis value)
    """
    
    if coordinates[0][0] == coordinates[1][0]:
        return True
    else:
        return False
    
    
def is_horizontal(coordinates):
    """
    If y1 == y2 then the line is horizontal (i.e. no change in y axis value)
    """
    
    if coordinates[0][1] == coordinates[1][1]:
        return True
    else:
        return False
    
    
def is_diagonal(coordinates):
    """
    If x1 - x2 == y1 - y2 then the line is diagonal (i.e. equal change in the x and y axis values)
    """
    
    # x1 should be the lowest of the x values and y1 should be lowest of y values
    x1 = coordinates[0][0]
    y1 = coordinates[0][1]
    x2 = coordinates[1][0]
    y2 = coordinates[1][1]
    
    
    if (abs(x2 - x1)) == (abs(y2 - y1)):
        
        return x1, y1, x2, y2


# Do the thing.
with open("input.txt", "r") as infile:
    lines = infile.read().splitlines()

    # Get data into list of lists of [[x1,y1], [x2,y2]] e.g. [[427, 523], [427, 790]] etc. Should find a neater way of doing this.   
    strings = [line.split(" -> ") for line in lines]
    string_pairs = [[j.split(",") for j in i] for i in strings]
    int_pairs = [[[int(k) for k in j] for j in i] for i in string_pairs]

# Determine size of matrix by maximum coordinate size
empty_matrix = np.zeros(max([[max(i) + 1 for i in j] for j in int_pairs]))


for vals in int_pairs:
    
    # Is the line vertical? (x1 == x2)
    if is_vertical(vals):
        
        # y1 is the smallest and y2 the biggest of the pair
        y1, y2 = sorted([vals[0][1], vals[1][1]])
        # y is the same so can be either
        x = vals[0][0]
        
        # Update the grid. +1 to x2 as python indexing doesn't include the last index (e.g. [1:2] will only give row 1)
        empty_matrix[y1:y2+1, x] += 1
    
    # Is the line horizontal (y1 == y2)
    elif is_horizontal(vals):

        # x1 is the smallest and x2 the biggest of the pair
        x1, x2 = sorted([vals[0][0], vals[1][0]])
        # x is the same so can be either
        y = vals[0][1]

        # Update the grid. +1 to y2 as python indexing doesn't include the last index (e.g. [1:2] will only give row 1)
        empty_matrix[y, x1:x2+1] += 1
    
    # Is the line diagonal? (x1 - x2 == y1 - y2)
    elif is_diagonal(vals):
        
        x1,y1,x2,y2 = is_diagonal(vals)
        
        # Account for all directions of lines as well as increasing/decreasing ranges using reversed() function. Bit clunky.
        if (x1 > x2) & (y1 < y2):
            for x, y in zip(range(x2, x1+1), reversed(range(y1, y2+1))):
                empty_matrix[y,x] += 1

        elif (x1 > x2) & (y1 > y2):
            for x, y in zip(range(x2, x1+1), range(y2, y1+1)):
                empty_matrix[y,x] += 1
                
        elif (x1 < x2) & (y1 < y2):
            for x, y in zip(range(x1, x2+1), range(y1, y2+1)):
                empty_matrix[y,x] += 1
                
        elif (x1 < x2) & (y1 > y2):
            for x, y in zip(range(x1, x2+1), reversed(range(y2, y1+1))):
                empty_matrix[y,x] += 1

print((empty_matrix > 1).sum())