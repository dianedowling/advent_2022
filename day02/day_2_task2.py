def choose_shape(elf, outcome):
    if outcome == 'Y': #draw
        if elf == 'A':
            shape = 'X'
        elif elf == 'B':
            shape = 'Y'
        else:
            shape = 'Z'
    elif outcome == 'X': #lose
        if elf == 'A':
            shape = 'Z'
        elif elf == 'B':
            shape = 'X'
        else:
            shape = 'Y'
    else: #win
        if elf == 'A':
            shape = 'Y'
        elif elf == 'B':
            shape = 'Z'
        else:
            shape = 'X'
    return shape    
    

def play_rps():
    weights = {'X':1, 'Y':2, 'Z':3}
    game_total = 0
    round_total = 0
    f = open('day_2.txt', 'r')
    for row in f:
        elf = row[0]
        outcome = row[2]
        me = choose_shape(elf, outcome)
        if (elf == 'A' and me == 'X') or (elf == 'B' and me == 'Y') or (elf == 'C' and me == 'Z'):
            round_total = 3 + weights[me] #draw
        elif (elf == 'A' and me == 'Z') or (elf == 'B' and me == 'X') or (elf == 'C' and me == 'Y'):
            round_total = 0 + weights[me] #lose
        else:
            round_total = 6 + weights[me] #win
        game_total += round_total
        round_total = 0
    print(game_total)



if __name__ == '__main__':
    play_rps()
