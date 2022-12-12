def play_rps():
    weights = {'X':1, 'Y':2, 'Z':3}
    game_total = 0
    round_total = 0
    f = open('day_2.txt', 'r')
    for row in f:
        elf = row[0]
        me = row[2]
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
