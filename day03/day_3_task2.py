def get_priority(item):
    ascii_code = ord(item)
    if ascii_code >= 97:
        priority = ascii_code - 96
    else:
        priority = ascii_code - 38
    return priority
    

def find_badge():
    total = 0
    i = 0
    f = open('day_3.txt', 'r')
    eof = False
    while not eof:
        line = f.readline().strip()
        if line == '':
            eof = True
        else:
            sack1 = set(line)
            sack2 = set(f.readline().strip())
            sack3 = set(f.readline().strip())
            duplicates = sack1 & sack2 & sack3 # set intersection
            for item in duplicates: # there should be only one! 
                priority = get_priority(item)
                total += priority
    print(total)



if __name__ == '__main__':
    find_badge()
