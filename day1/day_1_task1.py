def find_greediest():
    highest = 0
    this_elf = 0
    f = open('day_1.txt', 'r')
    for row in f:
        if row != '\n':
            this_elf += int(row)
        else:
            if this_elf > highest:
                highest = this_elf                
            this_elf = 0         
    print(highest)


if __name__ == '__main__':
    find_greediest()
