import pandas as pd

# I'm sorry.

with open("input.txt", "r") as binary:

    seq = binary.read().splitlines()
    
    seq = pd.DataFrame(seq, dtype="str")

    nn = len(seq[0][0])

    # This is disgusting and honestly I feel bad that it came to this...
    # str.split seems to put in strange empty columns at the start and end, so nn is required to limit this but it still adds an extra empty first column, so i just drop it here.
    seq = seq[0].str.split("", expand = True, n = nn).iloc[:,1:]

    ox_gen = seq
    co2_scbr = seq

    for col in ox_gen.columns:
        most_common = ox_gen[col].value_counts().index[0]
        ox_gen = ox_gen[ox_gen[col].str.contains(most_common)]
        if len(ox_gen) == 1:
            break

    for col in co2_scbr.columns:
        least_common = co2_scbr[col].value_counts().index[1]
        co2_scbr = co2_scbr[co2_scbr[col].str.contains(least_common)]
        if len(co2_scbr) == 1:
            break

    ox_gen = ox_gen.iloc[0].to_list()
    co2_scbr = co2_scbr.iloc[0].to_list()

    ox_gen = int(''.join(ox_gen),2)
    co2_scbr = int(''.join(co2_scbr),2)

    print(ox_gen * co2_scbr)