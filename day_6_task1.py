def find_marker():    
    f = open('day_6.txt', 'r')
    data = f.read()
    for i in range(len(data)):
        marker = data[i:i+4]
        unique_chars = set(marker)
        if len(unique_chars) == 4:
            print(i+4)
            break




if __name__ == '__main__':
    find_marker()
