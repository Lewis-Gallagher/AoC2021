import more_itertools
import sys

def pairwise(seq, window_size):
    
    up_count = 0
    win_sums = []
    
    # Convert list of strings to ints
    seq = [int(i) for i in seq.read().splitlines()]
    
    # Get sums of window sizes
    for i in range(len(seq) - window_size + 1):
        win_sum = sum(seq[i: i + window_size])
        win_sums.append(win_sum)
        
    # Iterate over pairwise and compare numbers
    for i, j in more_itertools.pairwise(win_sums):
        if i < j:
            up_count += 1
    
    return up_count
    
    
def main():
    with open(sys.argv[1], "r") as depth:
        print(pairwise(depth, int(sys.argv[2])))

if __name__ == "__main__":
    main()
