def count_overlaps():
    count = 0
    f = open('day_4.txt', 'r')
    for row in f:
        row=row.strip()
        row_pairs = row.split(",")
        pair_list = []
        for room_range in row_pairs:
            pair_list.append(room_range.split("-"))
        if (int(pair_list[0][0]) >= int(pair_list[1][0]) and int(pair_list[0][0]) <= int(pair_list[1][1])) or (int(pair_list[1][0]) >= int(pair_list[0][0]) and int(pair_list[1][0]) <= int(pair_list[0][1])):
            count +=1
    print(count)


if __name__ == '__main__':
    count_overlaps()
