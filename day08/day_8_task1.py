SIZE = 99

def build_array(forest):
    f = open('day_8.txt', 'r')
    for line in f:
        row = []
        line = line.strip()
        for tree in line:
            row.append(tree)
        forest.append(row)


def check_visibility(forest):
    number_visible = (4 * SIZE) - 4 # perimeter       
    for row in range(1, SIZE-1):
        for col in range(1, SIZE-1):
            tree = forest[row][col]
            #check left
            visible = True
            i = col - 1
            while visible and i >= 0:
                if forest[row][i] < tree:
                    i -= 1
                else:
                    visible = False
            if not visible: #check right
                visible = True
                i = col + 1
                while visible and i < SIZE:
                    if forest[row][i] < tree:
                        i += 1
                    else:
                        visible = False
            if not visible: #check above
                visible = True
                i = row - 1
                while visible and i >= 0:
                    if forest[i][col] < tree:
                        i -= 1
                    else:
                        visible = False
            if not visible: #check below
                visible = True
                i = row + 1
                while visible and i < SIZE:
                    if forest[i][col] < tree:
                        i += 1
                    else:
                        visible = False
            if visible:
                number_visible += 1
    print(number_visible)  
    

if __name__ == '__main__':
    forest = []
    build_array(forest)
    check_visibility(forest)
    
    
