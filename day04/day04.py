import pandas as pd
import numpy as np

def is_winner(card, numbers):
    """
    Takes a bingo card pandas dataframe and a list of numbers.
    Returns the index of the winning number (not the number itself) and the score of the card upon winning.
    """
    
    for index, num in enumerate(numbers):
        
        # Check if number anywhere in the card
        if num in np.array(card):
            
            # replace the number with np.nan
            card.replace(num, np.nan, inplace = True)
            
            # Win? Are any rows or columns all nan?
            if (card.isnull().all(axis = 0).any()) or \
               (card.isnull().all(axis = 1).any()):
                
                # Calculate the score of the winning card - fill nan with 0 and convert to np array, then sum.
                card = card.fillna(0).to_numpy()
                score = int(card.sum() * num)

                # return the index of the winning number and the score
                return index, score
            
            
def main():
    
    # Get first line into a list of integers
    with open("input.txt", "r") as infile:
        num_string = infile.read().splitlines()[0]
        numbers = [int(num) for num in num_string.split(",")]

    # Skip first row, read into large dataframe
    bingo_cards = pd.read_csv("input.txt", skiprows = 1, header = None, sep = ",", dtype={"0":np.int32})
    bingo_cards = bingo_cards[0].str.split(expand = True)

    # Generate list of dataframes
    card_li = []
    for i in range(0, len(bingo_cards), 5):
        card_li.append(bingo_cards[i:i+5].astype("int"))
        
    # Empty list for winners
    winners = []

    # Loop over each card in the list
    for card in card_li:

        # Append winning cards and index of winning number in numbers list
        win_card, win_index = is_winner(card, numbers)
        winners.append([win_card, win_index])

    # Get the lowest number in winners list.  i.e. the score that won first.
    print(min(num for num in winners))

    # Get the highest number in winners list.  i.e. the score that won last.
    print(max(num for num in winners))
    
if __name__ == "__main__":
    main()