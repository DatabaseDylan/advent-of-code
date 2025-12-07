def count_adjacent_rolls(current_roll_index: int, paper_rolls: tuple[str]) -> int:
    indexes_to_check = [-138,-137,-136,1,138,137,136,-1]
    adjacent_rolls = 0

    # Legend: 
    # -138  = top left
    # -137  = top
    # -136  = top right
    # 1     = right
    # 138   = bottom right
    # 137   = bottom
    # 136   = bottom left
    # -1    = left

    for index in indexes_to_check:

        search_index = index + current_roll_index

        # ignore out of range towards the beginning
        if search_index < 0:
            continue

        # ignore out of range towards the end
        if search_index >= len(paper_rolls):
            continue
        
        # new lines (to the left or right of a roll) do not count as empty spaces
        if (paper_rolls[search_index]) == '\n':
            continue
        
        # track adjacent rolls
        if (paper_rolls[search_index]) == '@':
            adjacent_rolls += 1

    return adjacent_rolls

def main():
    with open('paper_rolls.txt', 'r') as file:
        paper_rolls = tuple(file.read())

    rolls_to_move = 0 

    i = 0
    for roll in paper_rolls:
        # If the current index is not a roll, we can just skip early
        if roll != '@':
            i += 1
            continue
        adjacent_rolls = count_adjacent_rolls(current_roll_index=i,paper_rolls=paper_rolls)

        if adjacent_rolls < 4:
            rolls_to_move += 1

        i += 1

    print(rolls_to_move)

if __name__ == '__main__':
    main()