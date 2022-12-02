def find_top_three():
    highest_three = [0,0,0]
    this_elf = 0
    f = open('day_1.txt', 'r')
    for row in f:
        if row != '\n':
            this_elf += int(row)
        else:
            minimum = min(highest_three)
            if this_elf > minimum:
                highest_three.remove(minimum)
                highest_three.append(this_elf)
            this_elf = 0
    print(sum(highest_three))



if __name__ == '__main__':
    find_top_three()
