# %time

import timeit

def count_fish(starting_fish, days):
    
    # Create a list of zeros representing counts of fish states 0-8
    arr = [int(0) for i in range(0,9)]
    
    # Count the number of fish in each state
    for i in starting_fish:
        arr[i] += 1
    
    # For each day
    for i in range(0, days):

        # Remove the count of the fish at state 0 with pop() and add it to state 8 with append()
        new_fish = arr.pop(0)
        arr.append(new_fish)
        
        # Fish with state of 0 recycle to state 6
        arr[6] += new_fish

    return sum(arr)


with open("input.txt", "r") as f:
    input_data = [int(i) for i in f.read().split(',')]

test_data = [3,4,3,1,2]

assert count_fish(test_data, 18) == 26
assert count_fish(test_data, 80) == 5934 

print(f"Part 1: {count_fish(input_data, 80)}")
print(f"Part 2: {count_fish(input_data, 256)}")