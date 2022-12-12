def get_priority(item):
    ascii_code = ord(item)
    if ascii_code >= 97:
        priority = ascii_code - 96
    else:
        priority = ascii_code - 38
    return priority
    

def find_duplicates():
    total = 0
    f = open('day_3.txt', 'r')
    for row in f:
        num_items = len(row)
        half_way = int(num_items/2)
        compartment_1 = set(row[:half_way])
        compartment_2 = set(row[half_way:])
        duplicates = compartment_1 & compartment_2 # set intersection
        for item in duplicates: # there should be only one! 
            priority = get_priority(item)
            total += priority
    print(total)



if __name__ == '__main__':
    find_duplicates()
